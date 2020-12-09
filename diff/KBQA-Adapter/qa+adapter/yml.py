import yaml, os, sys

target = sys.argv[1]
os.makedirs('hr-bubo', exist_ok=True)
os.makedirs('ad-bubo', exist_ok=True)

yml = yaml.load(open('config/baseline.yml'))
yml['model']['name'] = target

yml['run_op']['model_dir'] = '../model'
yml['run_op']['log_dir'] = '../log'

yml['data']['transX_embedding_path'] = '../Data/rel.emb.nre.txt'
yml['data']['train_path'] = '../Data/{0}.train.pkl'.format(target)
yml['data']['dev_path'] = '../Data/{0}.valid.pkl'.format(target)
yml['data']['test_path'] = '../Data/{0}.test.pkl'.format(target)

fw = open('hr-bubo/{0}.yml'.format(target), 'w')
fw.write(yaml.dump(yml))
fw.close()

yml = yaml.load(open('config/gan-all.yml'))
yml['model']['name'] = 'gan.all-'+target

yml['run_op']['model_dir'] = '../model'
yml['run_op']['log_dir'] = '../log'

yml['data']['transX_embedding_path'] = '../Data/rel.emb.nre.txt'
yml['data']['train_path'] = '../Data/{0}.train.pkl'.format(target)
yml['data']['dev_path'] = '../Data/{0}.valid.pkl'.format(target)
yml['data']['test_path'] = '../Data/{0}.test.pkl'.format(target)

fw = open('ad-bubo/{0}.yml'.format(target), 'w')
fw.write(yaml.dump(yml))
fw.close()
