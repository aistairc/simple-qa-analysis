# revised code
Though we tried to use original codes, sometimes they contain minor bugs which make our experiment stop.
Moreover, we need to add some additional scripts to follow the instruction in their paper.
This folder contains revised codes used in our experiments, and this document explains why they are revised.

## BuboQA
### train.py, top_retrieval.py
- we revised a minor bug about the threshold setting in NumPy.

## KBQA-Adapter
### prepare_input.py, down_emb.sh
- we added them to prepare embeddings and QA dataset pickles for KBQA-Adapter

### Item.py
- we copied this file for avoiding dependency problems

### yml.py
- we added it to generate a configuration file automatically

### applyingbuboentity.py, applyingrerank.py, bubo_convert.py, load_data.py
- we wrote and revised them to follow the instruction for Entity Re-Ranking at the HR-BiLSTM paper and to generate a result file of BuboQA-format

### run_op.py
- additional lines were written to print scores of predicted relations

### start.py, network.py, FileUtil.py
- we revised them to fix minor bugs

## KEQA_WSDM19
### main.sh
- we added some lines to download embeddings

### train_entity.py, train_pred.py
- some arguments are added to divide working folders

### test_main.py
- we wrote additional lines to print each intermediate result of submodules
