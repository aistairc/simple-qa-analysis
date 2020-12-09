import os, pickle, yaml, sys
from collections import defaultdict
from Item import Item

path = '../Data/'
plist = os.listdir(path)

dlist = os.listdir('./')
os.makedirs('bubo_format', exist_ok=True)

rel2name = pickle.load(open('../Data/Embedding/rel.voc.pickle', 'rb'))
sub2rel = pickle.load(open('../Data/Embedding/subject2relation.pickle', 'rb'))

def load_buboentity(target):
  ent_dict = defaultdict(dict)
  for line in open('../../BuboQA/entity_linking/{0}/lstm/test-h100.txt'.format(target), encoding='utf-8'):
    tokens = line.strip().split(' %%%% ')
    tokens[0] = tokens[0].split('-')[-1]
    if len(tokens) < 2: ent_dict[tokens[0]] = []
    else:
      for token in tokens[1:]:
        if len(ent_dict[tokens[0]]) == 50: break
        ent_dict[tokens[0]][token.split('\t')[0][3:]] = float(token.split('\t')[-1])
  return ent_dict

def load_relscore(target):
  rel_dict = defaultdict(dict)
  for line in open('{}/rel.all.txt'.format(target), encoding='utf-8'):
    tokens = line.strip().split('\t')
    rel_dict[tokens[0]][rel2name[int(tokens[1])]] = float(tokens[2])
  return rel_dict

def reranking(target, ent_dict, rel_dict, qid2ans):
  fw = open(os.path.join('bubo_format', target + '.txt'), 'w')
  fw2 = open(os.path.join('ent_list', target + '.txt'), 'w')
  fw3 = open(os.path.join('ent_list', target + '.50.txt'), 'w')
  for qid in ent_dict:
    for entity in ent_dict[qid]:
      rel_score = dict()
      cand_rel = sub2rel[entity] 
      for crel in [rel2name[int(c)] for c in cand_rel]:
        if crel in rel_dict[qid]:
          rel_score[crel] = 0.1 * rel_dict[qid][crel]
      max_rel_score = max(rel_score.values()) if rel_score.values() else 0
      ent_dict[qid][entity] = (ent_dict[qid][entity]**0.6) * (max_rel_score**0.1)
    if not ent_dict[qid]: 
      fw2.write('{0}\t{1}\n'.format(qid, None))
      continue
    suitable_entity = sorted(ent_dict[qid].items(), key=lambda x: x[1], reverse=True)

    for i in range(50):
      if i == len(suitable_entity): break
      fw3.write('{0}\t{1}\t{2}\n'.format(qid, suitable_entity[i][0], suitable_entity[i][1]))

    suitable_entity = suitable_entity[0][0]
    fw2.write('{0}\t{1}\n'.format(qid, suitable_entity))
    cand_rel = [rel2name[int(c)]for c in sub2rel[suitable_entity]]
    suitable_relation = [(crel, rel_dict[qid][crel]) for crel in cand_rel if crel in rel_dict[qid]]
    suitable_relation = sorted(suitable_relation, key=lambda x: x[1], reverse=True)[:5]

    if not suitable_relation: continue
    for rel in suitable_relation:
      fw.write('test-{0} %%%% fb:{1} %%%% {2} %%%% {3}\n'.format(qid, rel[0], int(rel[0] == qid2ans[qid]), rel[1]))

  fw.close()
  fw2.close()
  fw3.close()
  return 1

def converting(dir, rel_dict, qid2ans):
  target = os.path.join(dir, 'all.output.txt')
  if os.path.exists(target):
    f = os.path.join('bubo_format', dir +  '.txt')
    fw = open(f, 'w', encoding='utf-8')
    for qid in rel_dict:
      cand_rel = [(crel, rel_dict[qid][crel]) for crel in rel_dict[qid]]
      cand_rel = sorted(cand_rel, key=lambda x: x[1], reverse=True)[:5]
      for crel, score in cand_rel:
        fw.write('test-{0} %%%% fb:{1} %%%% {2} %%%% {3}\n'.format(qid, crel, int(crel == qid2ans[qid]), score))
    fw.close()
  return 1


def load_goldanswer(target):
  qid2ans = dict()
  yml_path = '../qa+adapter/{0}-bubo/{1}.yml'
  if 'gan.all-' in target:
    yml_path = yml_path.format('ad', target.replace('-0', '').replace('gan.all-',''))
  else:
    yml_path = yml_path.format('hr', target.replace('-0', '').replace('gan.all-',''))

  yml = yaml.load(open(yml_path))
  test_path = yml['data']['test_path']

  test = pickle.load(open(test_path, 'rb'))
  for t in test:
    qid2ans[t.qid] = rel2name[t.relation]

  return qid2ans

def main():
  os.makedirs('bubo_format', exist_ok=True)
  os.makedirs('ent_list', exist_ok=True)
  for dir in dlist:
    if '-0' not in dir: continue
    ent_dict = load_buboentity(dir.replace('-0', '').replace('gan.all-', ''))
    rel_dict = load_relscore(dir)
    qid2ans = load_goldanswer(dir)
    if sys.argv[1] == 'rerank':
      reranking(dir, ent_dict, rel_dict, qid2ans)
    elif sys.argv[1] == 'convert':
      converting(dir, rel_dict, qid2ans)
    else: print("error argv")

if __name__ == '__main__':
  main()

