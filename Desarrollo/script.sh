#!/bin/bash

# Archivos
accessions="../DATOS/Accessions.txt"
busca="../DATOS/proka_nombre_accesion_ftp.txt"
guarda="../RESULTADOS/resultados_accesiones_buscadas.txt"

# Buscar y almacenar los resultados en el archivo
grep -F -f "$accessions" "$busca" > "$guarda"

# Mostrar archivo
more "$guarda"
