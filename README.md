[![build](https://github.com/sciling/qatransfer/actions/workflows/build.yml/badge.svg)](https://github.com/sciling/qatransfer/actions/workflows/build.yml)

## Install as package with pip

This repository is a fork of the [qa-tranfer](https://github.com/shmsw25/qa-transfer) repo with some bug fixes.
In addition, it adds a setup.py file so that it can be installed with pip:

```sh
  pip install "https://github.com/sciling/qatransfer/archive/refs/heads/master.zip#egg=qatransfer"
```
Please note that we tried not to change the structure of the original repo.
The main purpose is to be installed in [kubeflow components](https://kubeflow-pipelines.readthedocs.io/en/latest/source/kfp.components.html#:~:text=packages_to_install).
Thus, the package will not be installed in a clean way, i.e. there will be basic, wikiqa, semeval, etc packages after the installation.
To install it in a kubeflow component:
```python
func_to_container_op(your_component_function,  base_image='sciling/tensorflow:0.12.0-py3',
                     packages_to_install=["https://github.com/sciling/qatransfer/archive/refs/heads/master.zip#egg=qatransfer"])
```


## Question Answering through Transfer Learning


- This is the original implementation of "Question Answering through Transfer Learning from Large Fine-grained Supervision Data". [[paper](http://aclweb.org/anthology/P17-2081)] [[poster](https://shmsw25.github.io/assets/acl2017_poster.pdf)]
- Most parts were adapted & modified from "Bi-directional Attention Flow". [[paper](https://arxiv.org/pdf/1611.01603.pdf)] [[code](https://github.com/allenai/bi-att-flow)]
- Evaluation scripts for SemEval were adapted & modified from [SemEval-2016 official scorer](http://alt.qcri.org/semeval2016/task3/index.php?id=data-and-tools).
- Please contact [Sewon Min](https://shmsw25.github.io) ([email](mailto:shmsw25@snu.ac.kr)) for questions and suggestions.


Codes include

- pretraining BiDAF (span-level QA) and BiDAF-T (sentence-level QA) on SQuAD
- training on WikiQA
- training on SemEval-2016 (Task 3A)

### 0. Requirements

General
- Python3 (verified on 3.5.2.)
- Python2 (verified on 2.7.12., only for Semeval-2016 Scorer)
- unzip, wget (for running download.sh only)

Python Packages
- tensorflow (deep learning library, only works on r0.11)
- nltk (NLP tools, verified on 3.2.1)
- tqdm (progress bar, verified on 4.7.4)
- jinja2 (for visaulization; if you only train and test, not needed)

### 1. Quick Tutorial

First, download data (SQuAD, WikiQA, SemEval-2016, GLoVe, NLTK). This will download files to `$HOME/data`. Also, preprocess data and save them in `data`.
```
chmod +x download.sh; ./download.sh
chmod +x prepro.sh; ./prepro.sh
```

Then, pretrain the model on SQuAD.
```
chmod +x pretrain.sh
./pretrain.sh span 		# to pretrain BiDAF on SQuAD
./pretrain.sh class		# to pretrain BiDAF-T on SQuAD-T
```
You can use trained model from [original BiDAF code](https://github.com/allenai/bi-att-flow). Just place saved directory to `out/squad/basic/00`.

Finetune the model on WikiQA / Semeval.
```
chmod +x train.sh; ./train.sh DATA finetune RUN_ID PRETR_FROM STEP
```
- `DATA`: [`wikiqa` | `semeval]`
- `RUN_ID`: run id for finetuning. use unique run id for the same data.
- `PRETR_FROM`: [`basic` | `basic-class]`. use `basic` for span-level pretrained model, and `basic-class` for class-level pretrained model.
- `STEP`: global step of pretrained data. For a quick start, use `18000` for span-level pretrained model and `34000` for class-level pretrained model. However, monitoring tensorboard and pick the best global step is recommended, because results would depend much on the quality of pretrained model.

Finally, evaluate your model.
```
chmod +x evaluate.sh; ./evaluate.sh DATA RUN_ID START_STEP END_STEP
```
- `DATA`: [`wikiqa` | `semeval`]
- `RUN_ID`: run_id you used for finetuning
- `START_STEP`: STEP+200 when you used for finetuning
- `END_STEP`: STEP+5000

This is just for a quick tutorial. Please take a look at [run.md](run.md) for details about running the code.



