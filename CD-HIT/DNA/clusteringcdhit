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
#$ -N RUNvsearch
#
# Send an email after the job has finished
#$ -m e
#$ -M mar...7@outlook.com
#
#
# Resources of compute
# -pe 10
# -l mem=20
#
# output files to run
#
#$ -o ../cdhit90_output.$JOB_ID.out # Salida estandar
#$ -e ../cdhit90_output.$JOB_ID.err # Archivo con los errores
#
# If modules are needed, source modules environment (Do not delete the next line):
. /etc/profile.d/modules.sh
#
# Add any modules you might require:
module load cd-hit...
#
# Write your commands in the next line

$PWD="dir/datos/base"
cd-hit -i $PWD/ANALYSIS_CDHIT/psedomonasIMGconcatenados.genes.faa -o $PWD/ANALYSIS_CDHIT/RESULTSCLUSTERCDHIT/pseudocluster -c 0.90 -n 10 -M 20000 -d 0 -T 8
