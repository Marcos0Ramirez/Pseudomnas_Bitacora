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
#$ -N python_grcopred
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
#$ -o ../CONFUGRAF/pyconfusion_output.$JOB_ID.out # Salida estandar
#$ -e ../CONFUGRAF/pyconfusion_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
. /etc/profile.d/modules.sh
#
# Add any modules you might require:

#
# Write your commands in the next line
python2 RandomForest.py
