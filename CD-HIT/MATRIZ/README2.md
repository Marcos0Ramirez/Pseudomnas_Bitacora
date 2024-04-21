# 20 de abril del 2024
Ahora se vera como desarrollar el script para que corrar mas rapido el analisis y no tenga que estar abriendo los archivos a cada rato y haviendo busquedas tan largas

1. Para ello se piensa crear una tabla con todas las accesiones y que desdes ahi haga la busqueda
2. sustituir sed por otra funcion

```
#!/bin/bash

DIR="/mnt/c/Users/52477/Desktop/Descargas_NCBI"
MATRIXCDOUT="CDHIT/MATRIXDATA"
DATA="CDHIT/TODOS/clusterprotcatALL2000.clstr"

#Prueba rapida para el final del codigo
head -n 30 $DIR/$DATA > "$DIR/CDHIT/TODOS/30rengclusterprotcatALL2000.clstr"
DATA="CDHIT/TODOS/30rengclusterprotcatALL2000.clstr"
rm "$DIR/$MATRIXCDOUT/clust2.tmp"
#ls $DIR/$MATRIXCDOUT
#head -n 10 $DIR/$DATA

# Patrón para identificar el inicio de un nuevo cluster
patron1=">Cluster"
patron2="[0-9]+aa"
ni=0
nfinal=$(grep -E "$patron1" $DIR/$DATA | wc -l)
nfinal=$((nfinal-1))
echo $nfinal
# Iterar sobre el archivo
cd $DIR/IMGPSEUDOMONASGENOMES
echo "idgenomas" > $DIR/$MATRIXCDOUT/matriz2.txt
ls | tr '\s' '\n' >> $DIR/$MATRIXCDOUT/matriz2.txt
# cat $DIR/$MATRIXCDOUT/matriz.txt
while [[ $ni -le $nfinal ]]; do
        limitei=$(grep -o -n -w "Cluster $ni" $DIR/$DATA | grep -Eo "^[0-9]+")
        nf=$((ni+1))
        limitef=$(grep -o -n -w "Cluster $nf" $DIR/$DATA | grep -Eo "^[0-9]+")
        limitei=$((limitei+1))
        limitef=$((limitef-1))
        if [ $limitef != "-1" ]; then
        clusterset=$(sed -n "$limitei,${limitef}p" "$DIR/$DATA")
        else
        echo "ultimoski pa"
        ult=$(tail -n 1 $DIR/$DATA)
        limitef=$(grep -n "$ult" $DIR/$DATA | grep -o "^[0-9]*")
        clusterset=$(sed -n "$limitei,${limitef}p" "$DIR/$DATA")
        fi
        pizzitas=""
        pizzitas="$pizzitas\t$ni"
        while M= read -r  lineas; do
                busqueda=$(echo "$lineas" | grep -E -o -w ">[0-9]+")
                #echo "$busqueda"
                queso=$(grep -l "$busqueda" */*faa | grep -Eo "^[0-9]+")
                pizzitas="$pizzitas\n$queso"
        done <<< "$clusterset"


        echo "$ni" > "$DIR/$MATRIXCDOUT/clust2.tmp"
        cont=""
        echo "$ni"
        for i in *
        do
                reps=$(echo -e "$pizzitas" | grep -o "$i" | wc -l)
                cont="$cont\n$reps"
                echo "$i: $reps"
        done
        n=$(ls | tr '\s' '\n' | wc -l)
        #n=$(($n-1))
        cont=$(echo -e "$cont" | tail -n $n)
        echo -e "$cont" >> "$DIR/$MATRIXCDOUT/clust2.tmp"
        paste $DIR/$MATRIXCDOUT/matriz2.txt $DIR/$MATRIXCDOUT/clust2.tmp > $DIR/$MATRIXCDOUT/matriz2.tmp && mv $DIR/$MATRIXCDOUT/matriz2.tmp $DIR/$MATRIXCDOUT/matriz2.txt
        head -n $n $DIR/$MATRIXCDOUT/matriz2.txt > $DIR/$MATRIXCDOUT/matriz2.tmp && mv $DIR/$MATRIXCDOUT/matriz2.tmp $DIR/$MATRIXCDOUT/matriz2.txt
        ni=$((ni+1))
done
echo "$ni"
echo "$nf"
echo "$limitei"
echo "$limitef"
```

En este momento se pretende entender como es que se puede extraer y guardarlos en una variable para trabajar con ello podemos guardar todas lad porteinas
Trabajamos dentro de la carpta donde estan los genomas
```
grep -E ">" */*faa > ../CDHIT/MATRIXDATA/200424_grepfaa.txt
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/bec1e382-0918-478a-831b-52d4197205b8)

Asi se guarda y podemos usar solo lo que necesitamos, las accesiones
```
grep -E -o ">[0-9]+" */*faa > ../CDHIT/MATRIXDATA/200424_grepfaa.txt
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/b74df911-cc88-45a1-911c-071b3e1aebb8)

```
grep -E -o ">[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}'
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/0711ea3c-38aa-4ab8-b21c-02d5bec4c7bd)

Lugar donde se guarda la salida
```
grep -E -o ">[0-9]+" */*faa | awk -F "/[0-9]+.genes.faa:>" '{print $1 ":" $2}' > ../CDHIT/MATRIXDATA/200424_grepfaa.txt
```

```
Asi permite que la busqueda solo tenga las accesiones id del genoma y de la proteina
Y por otra parte awk, con -F excluye lo que se encuentra en el patron y asi permite que la infor que este entre ellos se dividan en nuevos y sean impresos separados por ":"
```

Asi por otra parte con la tabla de salida de CD-HIT clusterprotcatALL2000.clstr:
```
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/66ae443b-10fd-4154-bd28-669690640026)

```
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr | awk -F "." '{print $1}'
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/af344cfc-13b6-4f6e-a9a5-c44801b9faed)

Asi con la salida de esta busqueda, podemos trabajar
```
awk -F ">" '{print $2}' clusterprotcatALL2000.clstr | awk -F "." '{print $1}' > ../MATRIXDATA/filtclusterprotcatALL2000.clstr
```
Y establecer como va a ser el conteo para guardarlo en la matriz
Por otra parte, vemos como actuaria `for` para leer las lineas de `filtclusterprotcatALL2000.clstr`
```
for i in $(cat filtclusterprotcatALL2000.clstr); do echo $i; done
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f8bb1bca-04c3-4bf8-aafc-764b9859ac3c)

Pero ahora lo que hacemos es quita el espacio para que aparezca asi
```
awk '{gsub(/\s/, "", $0); print}' filtclusterprotcatALL2000.clstr
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/692c174d-0df2-46c3-ab43-980b90d78af8)

Asi para guardarlo en el mismo archivo, solo lo movemos
```
awk '{gsub(/\s/, "", $0); print}' filtclusterprotcatALL2000.clstr > tmp.tmp && mv tmp.tmp filtclusterprotcatALL2000.clstr
```
Finalmente solo para comprobar que tanto tiempo puee tardar con hacer busquedas con un `for` y `grep`.
```
date +%H:%M:%S && for i in $(cat filtclusterprotcatALL2000.clstr); do grep "$i" 200424_grepfaa.txt | grep -E "^[0-9]+" >> tmp.tmp; done && date +%H:%M:%S
```
Si tenemos un total de lineas `grep -v -c "Cluster" filtclusterprotcatALL2000.clstr`: `56287`
Con un inicio de horas `23:37:04` y termino a las ``








