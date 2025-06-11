

#!/bin/bash
#SBATCH --job-name=dask_job
#SBATCH --account=plgnatix02
#SBATCH --partition=plgrid
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=dask_job_%j.out


module load Anaconda3/2022.10
source activate dask-project
python notebooks/dask_slurm_analysis.py
