# simple-qa-analysis
Codes for reproducing the results shown in "An empirical analysis of existing systems and datasets toward general simple question answering" at COLING2020.

All codes and data will be prepared by just running `setup.sh`.
You can find launch scripts for each system in `/scripts`, and revised codes for each system in `/diff`.

## dependencies
python>3.6, virtualenv, and see `/req` for details.

## how to use
### to prepare QAKB systems and datasets
```
$ sh setup.sh
```
### run QAKB systems
```
$ cd scripts;sh run_{bubo|kbqa|keqa}.sh
```
Change $TARGET and $DATA in each script for your purpose.

## datasets
Free917, FreebaseQA, SimpleQuestions, and WebQSP will be prepared by `setup.sh`.

Filtered datasets for simple question answering, F917, FBQ, SQ, and WQ, can be found in `/datasets`.

## reference
- BuboQA
```
@inproceedings{mohammed-etal-2018-strong,
    title = "Strong Baselines for Simple Question Answering over Knowledge Graphs with and without Neural Networks",
    author = "Mohammed, Salman  and
      Shi, Peng  and
      Lin, Jimmy",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N18-2047",
    doi = "10.18653/v1/N18-2047",
    pages = "291--296"
}
```
- HR-BiLSTM
```
@inproceedings{yu-etal-2017-improved,
    title = "Improved Neural Relation Detection for Knowledge Base Question Answering",
    author = "Yu, Mo  and
      Yin, Wenpeng  and
      Hasan, Kazi Saidul  and
      dos Santos, Cicero  and
      Xiang, Bing  and
      Zhou, Bowen",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P17-1053",
    doi = "10.18653/v1/P17-1053",
    pages = "571--581"
}
```
- KBQA-Adapter
```
@inproceedings{peng19acl,
    title = {Learning Representation Mapping for Relation Detection in Knowledge Base Question Answering},
    author = {Peng Wu, Shujian Huang, Rongxiang Weng, Zaixiang Zheng, Jianbing Zhang, Xiaohui Yan and Jiajun Chen},
    booktitle = {The 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
    address = {Florence, Italy},
    month = {July},
    year = {2019}
}
```
- KEQA
```
@conference{Huang-etal19Knowledge,
    Title = {Knowledge Graph Embedding Based Question Answering},
    Author = {Xiao Huang and Jingyuan Zhang and Dingcheng Li and Ping Li},
    Booktitle = {ACM International Conference on Web Search and Data Mining},
    Year = {2019}
}
```

## acknowledgment
These works are based on results obtained from projects JPNP20006 and JPNP15009, commissioned by the New Energy and Industrial Technology Development Organization (NEDO), and also with the support of RIKEN–AIST Joint Research Fund (Feasibility study). 

