#!/bin/bash
# Use current working directory
#$ -cwd
#
# Join stdout and stderr
#$ -j y
#
# Run job through bash shell
#$ -S /bin/bash
#
#You can edit the scriptsince this line
#
# Your job name
#$ -N PYRANDOM
#
# Send an email after the job has finished
#$ -m e
#$ -M marcosuniramirez7@outlook.com
#
#
# Resources of compute
#$
#$ -l vf=20G
#
# output files to run
#
#$ -o /mnt/atgc-d3/sur/users/ENESL-MarcosR/PSEUDOMONAS_SCRIPTS/MicroSetRANDOMFOREST/OUTPUT/pyrandom_forgraph_output.$JOB_ID.out # Salida estandar
#$ -e /mnt/atgc-d3/sur/users/ENESL-MarcosR/PSEUDOMONAS_SCRIPTS/MicroSetRANDOMFOREST/OUTPUT/pyrandom_forgraph_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
. /etc/profile.d/modules.sh
#
# Add any modules you might require:

#
# Write your commands in the next line
python2 RandomForest_addhist_logimp_python275_dosnichos.py


