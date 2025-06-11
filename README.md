# Large-scale-dataset-processing-using-Dask

## Table of contents:

- [General info](#general-info)
- [Description](#description)
- [Simulation functionalities](#simulation-functionalities)
- [Data analysis](#data-analysis)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)

### General info

This project was carried out by a 2-person team as part of the "Large Scale Computing" course at AGH University of Science and Technology.

The main goal of this project was to explore and evaluate the capabilities of Dask for processing large-scale datasets.

### Project structure

```
├── data/                     # Raw input data (NYC Yellow Taxi)
│
├── notebooks/                # Analysis in Pandas, Dask (local), Dask(cyfronet)
│
├── results/                  # Runtime benchmarks, memory usage, plots
│
├── cluster_config/           # Dask cluster setups (e.g., SLURM on Ares)
│
├── environment.yml           # Reproducible environment for Conda


```

### Requirements

All libraries and tools used in this project are specified in the [environment.yml file](environment.yml) for reproducibility.

### Setup

### Setup

1. First, clone this repository.
   ```sh
   git clone https://github.com/natix-x/Traffic-simulator.git
   cd Traffic-simulator
   ```
2. Create and activate working environment
   ```sh
    conda env create -f environment.yml
    conda activate dask-project
   ```
