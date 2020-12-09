import pickle, os, sys
from Item import Item
from collections import defaultdict

path = '../Data/'

def load_buboentity(target, model):
    ent_dict = {}
    path = '../model/ent_list/{}-0.txt'
    if model == 'ad':
        path = '../model/ent_list/gan.all-{}-0.txt'
    for line in open(path.format(target)):
        ent_dict[line.strip().split('\t')[0]] = line.strip().split('\t')[1]
    return ent_dict

def main():
    target = sys.argv[2]
    model = sys.argv[1]
    ent_dict = load_buboentity(target, model)
    pkl = pickle.load(open(path+target+".test.pkl", 'rb'))
    for p in pkl:
        p.subject = ent_dict.get(p.qid, '')
    pickle.dump(pkl, open(path+target+".test.pkl", 'wb'))


if __name__ == '__main__':
    main()
