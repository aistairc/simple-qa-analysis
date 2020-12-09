import pickle, os, sys
from Item import Item
from collections import defaultdict

path = '../Data/'

def load_buboentity(target):
    ent_dict = defaultdict(set)
    for line in open('../../BuboQA/entity_linking/{0}/lstm/test-h100.txt'.format(target), encoding='utf-8'):
        tokens = line.strip().split(' %%%% ')
        tokens[0] = 'test-' + tokens[0].split('-')[-1]
        if len(tokens) == 1: 
            ent_dict[tokens[0]] = []
        else:
            for token in tokens[1:]:
                if len(ent_dict[tokens[0]]) == 50: 
                    break
                ent_dict[tokens[0]].add(token.split('\t')[0][3:])
    return ent_dict

def main():
    target = sys.argv[1]
    ent_dict = load_buboentity(target)
    pkl = pickle.load(open(path+target+".test.pkl", 'rb'))
    for p in pkl:
        qid = 'test-' + str(p.qid)
        p.subject = list(ent_dict.get(qid, []))
    pickle.dump(pkl, open(path+target+".test.pkl", 'wb'))


if __name__ == '__main__':
    main()
