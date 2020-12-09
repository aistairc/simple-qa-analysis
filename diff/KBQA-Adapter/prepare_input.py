import pickle, itertools, os
from argparse import ArgumentParser

class Item:
    def __init__(self,qid, question, sub, relation, obj, gold_type, subject_text, anonymous_question):
        self.qid = qid
        self.question = question
        self.subject = sub
        self.relation = relation
        self.object = obj
        self.gold_type = gold_type
        self.subject_text = subject_text
        self.anonymous_question = anonymous_question
        self.num_text_token = len(question.split(" "))

    def add_candidate(self, sub, rels, types=None):
        if not hasattr(self, 'cand_sub'):
            self.cand_sub = []
        if not hasattr(self, 'cand_rel'):
            self.cand_rel = []
        if not hasattr(self, 'sub_rels'):
            self.sub_rels = []
        self.cand_sub.append(sub)
        self.sub_rels.append(rels)
        self.cand_rel.extend(rels)
        if types:
            if not hasattr(self, 'sub_types'):
                self.sub_types = []
            self.sub_types.append(types)

    def remove_duplicate(self):
        if hasattr(self,'cand_rel'):
            self.cand_rel = list(set(self.cand_rel))

result_path = 'Data'
parser = ArgumentParser()
parser.add_argument('--dataset', type=str, required=True)
args = parser.parse_args()

rel_dict = pickle.load(open('Data/Embedding/rel.voc.pickle', 'rb'))

for splits in ['train', 'valid', 'test']:
    res = '{0}/{1}.{2}.pkl'.format(result_path, args.dataset, splits)
    
    data = []
    for line in open('../datasets/{0}/{1}.txt'.format(args.dataset, splits)):
        tokens = line.strip().split('\t')

        question = tokens[5]
        sub = tokens[1][3:]
        sub_text = tokens[2]
        rel = rel_dict[tokens[3][3:]]
        obj = tokens[4][3:]
        qid = tokens[0].split('-')[-1]

        masked_tokens = tokens[6].split()
        indexes = [i for i, x in enumerate(masked_tokens) if x == 'I']

        mention = ' '.join([question.split()[i] for i in indexes])
        anonymous_question = question.replace(mention, 'X')

        data.append(Item(qid, question, sub, rel, obj, [], sub_text, anonymous_question))

    pickle.dump(data, open(res,'wb'))



