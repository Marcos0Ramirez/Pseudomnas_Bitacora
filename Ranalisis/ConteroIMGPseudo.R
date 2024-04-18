pseudos <- read.csv(file = "../Desktop/Descargas_NCBI/Pseudomonas_abietaniphila", header = FALSE)
print(pseudos[,1])
Busqueda <- grep("Pseudomonas", pseudos$V1)
BUS <- data.frame()
for (i in Busqueda) {
  BUS <- rbind(BUS, pseudos[i,1])
}

for (i in grep("Candidatus", BUS$X.Pseudomonas.abietaniphila.)) {
  print(i)
  BUS <- BUS[!(BUS[i,1]), ]
}

length(BUS[,1])
length(unique(BUS[,1]))


### Por ChatGPT, se mejoro el comando para que funcionara.
pseudos <- read.csv(file = "../Desktop/Descargas_NCBI/Pseudomonas_abietaniphila", header = FALSE)
print(pseudos[,1])
Busqueda <- grep("Pseudomonas", pseudos$V1)
BUS <- data.frame()
for (i in Busqueda) {
  BUS <- rbind(BUS, pseudos[i,1])
}

# Si el dataframe 'BUS' tiene solo una columna, renombramos la columna como 'X.Pseudomonas.abietaniphila.'
if(ncol(BUS) == 1) {
  colnames(BUS) <- "X.Pseudomonas.abietaniphila."
}

# Eliminar las filas que contienen "Candidatus" en la columna 'X.Pseudomonas.abietaniphila.'
for (i in grep("Candidatus", BUS$X.Pseudomonas.abietaniphila.)) {
  print(i)
  BUS <- BUS[-i, , drop = FALSE]
}
length(unique(BUS[,1]))
