# Large-scale-dataset-processing-using-Dask

## Table of contents:

- [General info](#general-info)
- [Data](#data)
- [Project structure](#Project-structure--main-components)
- [Requirements](#requirements)
- [Setup](#setup)

### General info

This project was carried out by a 2-person team as part of the "Large Scale Computing" course at AGH University of Science and Technology.

The main goal of this project was to explore and evaluate the capabilities of Dask for processing large-scale datasets.
Our focus was not on the data analysis itself, but rather on comparing and exploring functionality and performance of Dask - both on a local cluster and within a SLURM-managed HPC environment.

### Data

We selected the [TLC Trip Record Data - Yellow Taxi Trip Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) as an example of a large dataset. The analysis covers data from the years 2023 and 2024, each with approximately 40 million records.

Also some analysis was performed with other parquet files downloaded from [AWS public datasets](https://registry.opendata.aws/)

### Project structure - main components

```
├── data/                     # NYC Yellow Taxi data
│
├── parquet_files/            # Other big data examples (from AWS storage)
│
├── notebooks/                # Analysis in Pandas, Dask (local), Dask(cyfronet)
│
├── results/                  # Runtime benchmarks, memory usage, plots, slurm outputs
│
├── cluster_config/           # Dask cluster setups (e.g., SLURM on Athena)
│
├── utils/                    # Measure metrics & save results to CSV files

```

### Requirements

All libraries and tools used in this project are specified in the [requirements.txt](./requirements.txt) for reproducibility.

### Setup

If you want to further explore our project:

1. First, clone this repository.
   ```sh
   git clone https://github.com/natix-x/Large-scale-dataset-processing-using-Dask.git
   cd Large-scale-dataset-processing-using-Dask
   ```
2. Then create and activate working environment
   ```sh
    # for Windows users 
    VenvSetup.bat

    # for Linux/mcOS users
    venv_setup.sh
   ```

#### Dask SLURM analysis

1. Synchronizing your remote environment.

   Pleses remember to synchronize your local project with the remote environment. Adjust the [sync_project.sh](./sync_project.sh) script according to your setup. You can exculde some directories or files by modifying UNIX command (venv is excluded already).

   Then, if you prefer, you can edit files directory directly on the server using [VSCode Remote SSH](https://code.visualstudio.com/docs/remote/ssh) or work locally and run sync_project.sh whenever you want to update your remote environment

2. Launching Dask.

   For distributed tests, we used supercomputer Athena at Cyfronet (PLGrid infrustructure).

   You can lunch Dask on the same or different SLURM-based cluster. You just need to adjust the parameters of the SLURMCluster in the configuration file: [slurm_config.json](cluster_config/slurm_config.json).

   For more details and available options, please refer to the official [Dask Jobqueue documentation](https://jobqueue.dask.org/en/latest/generated/dask_jobqueue.SLURMCluster.html).

3. Perfoming analysis.
   
   Now you can perform analysis both in Jupyter notebooks and python files.
