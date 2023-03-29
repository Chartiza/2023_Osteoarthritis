#!/bin/bash
#SBATCH -J mrg-mOTUs
#SBATCH --partition=amd
#SBATCH -t 1:00:00
#SBATCH --error=mrg-mOTUs_err1
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --mail-user=<pantiukh@gmail.com>
#SBATCH --mail-type=BEGIN,END,FAIL

module load any/motus
out='/gpfs/space/home/pantiukh/2023_Osteoarthritis/'

motus merge -d /gpfs/space/home/pantiukh/2023_Osteoarthritis/motus/all/ > $out/mOTUs_merged_profiles1.txt

module purge
