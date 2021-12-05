# we assume that you have already python3 >= 3.5 and are abled to use virtualenv

# set up BuboQA
git clone https://github.com/castorini/BuboQA.git
cp -R -r diff/BuboQA/ ./
cd BuboQA
virtualenv --python=python3 bubo
. bubo/bin/activate
pip install -U pip
pip install -r ../req/req_bubo.txt
python -c "import nltk;nltk.download('treebank');nltk.download('stopwords')"
sh setup.sh
deactivate
cd ..

# set up HR-BiLSTM and KBQA-Adapter
git clone https://github.com/wudapeng268/KBQA-Adapter.git
cp -R -r diff/KBQA-Adapter/* ./
cd KBQA-Adapter
cd Data
sh down_dmb.sh
cd ..
virtualenv --python=python3 kbqa
. kbqa/bin/activate
pip install -U pip
pip install -r ../req/req_kbqa.txt
deactivate
cd ..

# set up KEQA
git clone https://github.com/xhuang31/KEQA_WSDM19.git
cp -R -r diff/KEQA_WSDM19/ ./KEQA_WSDM19/
cd KEQA_WSDM19
virtualenv --python=python3 keqa
. keqa/bin/activate
pip install -U pip
pip install -r ../req/req_keqa.txt
python -c "import nltk;nltk.download('treebank');nltk.download('stopwords')"
sh main.sh
deactivate
cd ..

# SimpleQuestions in BuboQA
mkdir datasets/SimpleQuestions
cp BuboQA/data/processed_simplequestions_dataset/* datasets/SimpleQuestions

# WebQSP
mkdir datasets/WebQSP
wget https://download.microsoft.com/download/F/5/0/F5012144-A4FB-4084-897F-CFDA99C60BDF/WebQSP.zip
unzip WebQSP.zip
cp WebQSP/data/WebQSP.train.json datasets/WebQSP
cp WebQSP/data/WebQSP.test.json datasets/WebQSP
rm -rf WebQSP*

# FreebaseQA
mkdir datasets/FreebaseQA
git clone https://github.com/kelvin-jiang/FreebaseQA.git
cp FreebaseQA/FreebaseQA-train.json datasets/FreebaseQA/FreebaseQA.train.json
cp FreebaseQA/FreebaseQA-dev.json datasets/FreebaseQA/FreebaseQA.valid.json
cp FreebaseQA/FreebaseQA-eval.json datasets/FreebaseQA/FreebaseQA.test.json
rm -rf FreebaseQA

# Free917
mkdir datasets/free917
git clone https://github.com/ad-freiburg/aqqu.git
cp aqqu/evaluation-data/free917.train.json datasets/free917/
cp aqqu/evaluation-data/free917.test.json datasets/free917/
rm -rf aqqu
