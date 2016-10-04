#! /bin/bash -l
#SBATCH -A b2011098
#SBATCH -M milou
#SBATCH -p core -n 16
#SBATCH -t 1-00:00:00
#SBATCH -J DATASETPIPE
#SBATCH -e DATASETPIPE_SLURM_Job_id_%j.stderr.txt
#SBATCH -o DATASETPIPE_SLURM_Job_id_%j.stdout.txt
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ferraxi@gmail.com

sh build_extended_dataset_pipeline.sh
