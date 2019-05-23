
# Multiagent ARN

## Installation instructions

This project based on [SMAC](https://github.com/oxwhirl/smac) and [pymarl](https://github.com/oxwhirl/pymarl)

OS: Ubuntu 14 or 16 

Install StarCraftII:

```shell
chmod 755 ./install_sc2.sh
./install_sc2.sh
tar -xvf SMAC_Maps_supply.tar.gz
mv SMAC_Maps/* 3rdparty/StarCraftII/Maps/SMAC_Maps/
```

You must install anaconda before installing code env.

Install Code Env: 

```shell
conda create -n ARN python=3.6
source activate ARN
conda install certifi==2018.8.24
pip install -r requirements.txt
```

## Run an experiment 

Activate Code Env:
```shell
source activate ARN
export PYTHONPATH=. 
```

Than:

### 8m:

#### IQL

##### Vanilla
```shell
python src/main.py --config=iql_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='dense_rnn' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

##### Attention
```shell
python src/main.py --config=iql_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='dense_rnn_attention' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

##### Dueling
```shell
python src/main.py --config=iql_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='dense_rnn_dueling' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

##### ARN
```shell
python src/main.py --config=iql_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='arn_rnn' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

#### VDN

##### Vanilla
```shell
python src/main.py --config=vdn_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='dense_rnn' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

##### Attention
```shell
python src/main.py --config=vdn_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='dense_rnn_attention' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

##### Dueling
```shell
python src/main.py --config=vdn_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='dense_rnn_dueling' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

##### ARN
```shell
python src/main.py --config=vdn_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 agent='arn_rnn' legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 seed=100
```

#### QMIX

##### Vanilla
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2' seed=100 agent='dense_rnn'
```

##### Attention
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2' seed=100 agent='dense_rnn_attention'
```

##### Dueling
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2' seed=100 agent='dense_rnn_dueling'
```

##### ARN
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=8m_8m agents_num=8 enemies_num=8 legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2' seed=100 agent='arn_rnn'
```


### 15m:

##### Vanilla
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=15m_15m agents_num=15 enemies_num=15 agent='dense' legal_action=False batch_size_run=4 use_tensorboard=True save_model=True runner_log_interval=2000 arn_hidden_size=64 seed=100
```

##### ARN
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=15m_15m agents_num=15 enemies_num=15 agent='arn' legal_action=False batch_size_run=4 use_tensorboard=True save_model=True runner_log_interval=2000 arn_hidden_size=64 seed=100
```

### 2s3z:

##### Vanilla
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=2s3z agents_num=5 enemies_num=5 legal_action=False batch_size_run=1 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2' type1_num=3 type2_num seed=5 agent='dense' dense_size=128
```

##### Mixed ARN
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=2s3z agents_num=5 enemies_num=5 legal_action=False batch_size_run=4 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2_sort' type1_num=3 type2_num=2 seed=5 agent='arn_diff_rnn'  arn_hidden_size=64
```

<!---
##### ARN
```shell
python src/main.py --config=qmix_smac --env-config=sc2 with env_args.map_name=2s3z agents_num=5 enemies_num=5 legal_action=False batch_size_run=4 use_tensorboard=True save_model=True runner_log_interval=2000 env='sc2_sort' type1_num=3 type2_num=2 seed=5 agent='arn_wo_share_diff'  arn_hidden_size=64
```
---->
