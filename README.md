# Large-scale-dataset-processing-using-Dask

## Table of contents:

- [General info](#general-info)
- [Data](#data)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Setup](#setup)

### General info

This project was carried out by a 2-person team as part of the "Large Scale Computing" course at AGH University of Science and Technology.

The main goal of this project was to explore and evaluate the capabilities of Dask for processing large-scale datasets.

### Data

We selected the [TLC Trip Record Data - Yellow Taxi Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) as an example of a large dataset. The analysis covers data from the years 2023 and 2024, each with approximately 40 million records.

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

If you want to further explore our project:

1. First, clone this repository.
   ```sh
   git clone https://github.com/natix-x/Large-scale-dataset-processing-using-Dask.git
   cd Large-scale-dataset-processing-using-Dask
   ```
2. Then create and activate working environment
   ```sh
    conda env create -f environment.yml
    conda activate dask-project
   ```

#### Dask SLURM analysis

For distributed tests, we used supercomputer Athena atCyfronet (PLGrid infrustructure).

If you want to launch Dask on a different SLURM-based cluster, you just need to adjust the parameters of the SLURMCluster in the configuration file: [slurm_config.json](cluster_config/slurm_config.json).

For more details and available options, please refer to the official [Dask Jobqueue documentation](https://jobqueue.dask.org/en/latest/generated/dask_jobqueue.SLURMCluster.html).
