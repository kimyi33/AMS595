
# AMS 595 - Final: Impact of Initial Node Features and Adjacency Normalization in GCN-Based Botnet Detection

This repository contains the implementation and experiments for the
final project. The project analyzes how different node feature
initialization strategies and adjacency normalization schemes affect the
performance of Graph Convolutional Networks (GCNs) on large-scale botnet
communication graphs.

## Objective
Using the public dataset and source code introduced by Zhou et al.
(2020), we systematically evaluate: 
* Node feature initialization
  - All-ones features
  - Integer-index features
* Identity features (attempted but infeasible at scale)
  - Adjacency normalization
  - Symmetric normalization
  - Random-walk normalization

The implementation is based on and extended from the official repository
by Zhou et al.: https://github.com/harvardnlp/botnet-detection

## Repository Structure
```
.
├── botdet/                 # Core library (models, datasets, loaders)
├── train_botnet.py         # Main training and evaluation script
├── run_botnet_ones_sm.sh   # Ones features + symmetric normalization
├── run_botnet_ones_rw.sh    # Ones features + random-walk normalization
├── run_botnet_int_sm.sh     # Integer-index features + symmetric normalization
├── run_botnet_int_rw.sh    # Integer-index features + random-walk normalization
├── setup.py                # Package setup file
├── AMS595_Project_Final.ipynb  # Jupyter notebook (experiment walkthrough)
├── saved_models/           # Training logs and saved checkpoints
└── README.md               # This file
```

## How to run the code
Simply run AMS595_Project_Final.ipynb
