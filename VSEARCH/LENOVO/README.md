# Manejo de datos local, para analizarlos
Para el dia 22 de marzo del 2024
se utilizo el comando siguiente
```
vsearch --cluster_fast ../../CDHIT/TODOS/fromscriptall.genes.faa --id 0.6 --centroids vsearPseudo.faa --clusterout_id --clusterout_sort --uc PseudoPrueba.uc
```
los cuales describen estas acciones
```
vsearch           | Llamar el programa para ejecutarlo
--cluster_fast    | Usa el archivo 'fromscriptall.genes.faa', donde estan las proteinas de cada organismo concatenadas en formato fasta, para finalmente clusterizar las proteinas por orden de longitud de las secuencias.
--id              | Aqui se puede especificar cual es la identidad minima por la cual se van a agrupar las proteinas para generar los clusters.
--centroids       | Especifica las secuencias centrales por las cuales se ocuparon para agrupar las demas.
--clusterout_id   | En el archivo de salida indicado por '--consout' agrega un id de agrupacion y a los archivos de perfil
--clusterout_sort | Ordena el perfil por abundancia de 'decr' en los archivos de salida indicados por los comnados '--msaout' y '--consout'
--uc              | Especifica el nombre del archivo de salida como lo haria el programa de tipo UCLUST (por similitud de las secuencias)
```
De lo anterior:
```
Como extra
--consout         | Exporta un archivo con las secuencias consenso para la agrupacion, en un archivo FASTA
--msout           | Exporta alineamientos multiples en un archivo FASTA
```

Muestra de parte de los resultados del comando anterior `PseudoPrueba.uc`
```
S       0       4856    *       *       *       *       *       2785749539      *
S       1       4480    *       *       *       *       *       2972001972      *
S       2       4271    *       *       *       *       *       2518032096      *
H       2       4239    73.1    +       0       0       13D150M6D213M7D241MD44M2D237M3D619M6I118M2D213MI68MI104M4I694MI69MD157M6I71M9I114M5I245M5I266M4I142M11I272M3I167M11I    2549670384      2518032096
H       2       4203    75.8    +       0       0       15D54M2D59M8I522MD748M3D269M17I164M2I120M4D335M5I145M3I94M5I54M12I253M6I42MD334M2I452M3I142M5I293M4I97M22I      2633066195      2518032096
H       2       4150    73.3    +       0       0       28D256MI91M2D48M8I287M2D346M7I291M4I106M4I14M4I110M6I241M2I68M9I73M9I207M3D104M22I219M2I127M3I27M7I113M3D94M4I168M2I353MI127M9I69MI252M7I250M2I71M45I   2923166973      2518032096
S       3       4029    *       *       *       *       *       2923170970      *
H       3       3665    69.4    +       0       0       136I116M5I214M9I92MD249M4I182M2D78MD89M2I147M3I180MD22M6I156M9D397M9I86M2I45M2I67M6I264M6I254MI353MI190MD144M6I63M6I159M3I103M172I      2714614382      2923170970
H       3       3657    69.0    +       0       0       265I220M8I394M4I181MD42M5D393M2I267M3D89MD431M7I165MD112M9I155M5I193MD87M8I195M14I122M2I366M4D71MI158M63I       2549668513      2923170970
H       3       3468    70.7    +       0       0       500I234M2I121MD174M7I146M3I90M2I189MD66M2I68M9I41M2I105M3I75M2I108M6I42M9I385M2I144M10I284MD148M6I504MI50MI123MD365M2D  2633066528      2923170970
S       4       3296    *       *       *       *       *       2923168233      *
H       4       3182    72.3    +       0       0       37I59M3I288M10I238M6I153MD56M2I25M3I203M2D245M2D49M9I469M8I93MD256M2D414M2I71MI134M3D98M3D87M2I102M2I128M43I    2972007055      2923168233
H       4       3049    70.7    +       0       0       58I171M13I352MI48M5I112M23I196M20I101MD223M3I274M6I271M3I118M8I54MD80M8I92M5I250M2I259M10I36M7I39MI298M2D48M3I23M75I    2556075033      2923168233
H       4       2968    73.0    +       0       0       122I178MD94M3I140M3I193M6I196MI30MI77MI245M3D61M4D584M2I240MI303M8I145M8I38M31I129MI72M14I109M2I126M132I        2714616755      2923168233
H       4       2963    71.2    +       0       0       260I186M4I30M2I65M10I113M2I107M8I169M3I126M2I78M7D248MI128M4I237M16I86M3D135M4I228MI91M16I238M5I156M2D178M3I149M3I203MI 8011073211      2923168233
H       4       2948    70.3    +       0       0       211I227M4D157M2D450M6I155M14I74M4I51M2I253MI111M13I109M9I105M13I160M12I241MD69M4D669MI67M2I39M71I       2972004231      2923168233
S       5       2934    *       *       *       *       *       2972004192      *
S       6       2903    *       *       *       *       *       2556078011      *
H       6       2847    74.4    +       0       0       37I308M3I139M9I172M7I83MI125M9I262MD289MD153M2D105M2I190M4I94MD502M2D239MD170M8D                               2923168179       25560780
11
```
Descripcion del archivo de salida, por columna. Descripcion en https://manpages.ubuntu.com/manpages/jammy/man1/vsearch.1.html
```
              --uc filename
                       Output  clustering  results  in filename using a tab-separated uclust-like
                       format with 10 columns and 3 different type of entries (S, H or  C).  Each
                       fasta sequence in the input file can be either a cluster centroid (S) or a
                       hit (H) assigned to a cluster. Cluster records (C)  summarize  information
                       (size, centroid label) for each cluster. In the context of clustering, the
                       option --uc_allhits has no effect  on  the  --uc  output.  Column  content
                       varies with the type of entry (S, H or C):

                              1.  Record type: S, H, or C.

                              2.  Cluster number (zero-based).

                              3.  Centroid length (S), query length (H), or cluster size (C).

                              4.  Percentage of similarity with the centroid sequence (H), or set
                                  to '*' (S, C).

                              5.  Match orientation + or - (H), or set to '*' (S, C).

                              6.  Not used, always set to '*' (S, C) or to zero (H).

                              7.  Not used, always set to '*' (S, C) or to zero (H).

                              8.  set to '*' (S, C) or, for  H,  compact  representation  of  the
                                  pairwise    alignment   using   the   CIGAR   format   (Compact
                                  Idiosyncratic Gapped Alignment Report): M  (match/mismatch),  D
                                  (deletion) and I (insertion). The equal sign '=' indicates that
                                  the query is identical to the centroid sequence.

                              9.  Label of the query sequence (H), or of  the  centroid  sequence
                                  (S, C).

                              10. Label of the centroid sequence (H), or set to '*' (S, C).
```
Salida del archivo `vsearPseudo.faa`
```
>2518034652;clusterid=461
MRKTAAAAGCAMTanmawvdstndrvardkrrdgrvsgshvvrdyvnggggsmggttvrcytdyhkagryvarsmamtar
ydakgvavryCM
>2633065095;clusterid=410
vrhwrgsssaasahagntrrraawdsgrrsraraskahgrrdaaahwahvsrsaranagahgwravrdaagrmanasstr
rrkdvasrdramashrvTRAGRWVTNAAGGCCTGGTarhrahasGDKGSV
>2518034247;clusterid=391
MDSRTASATARGGATvaaavhaasdarwvsdssTYVRSGTDGHRVGTKSGKTGSGnysvrgngdvwsndsvgsrdavadt
gknddswksrvgmtdsrkkdarnkandssrdtargdnkvmmrymvyGGSAGAGAGATRGRRKNDRW
>2505554406;clusterid=366
MKTVVTGAAGGGACarrgmaddkrvasgdayvvdtnsagmtysgrdvnnaaavvadtrsvssrnnvatrakrsndarvst
vsggvtsycaskgrgamsgdakgkvgstatdtmrkaggnaasddvarvmdkcrtkssassamnrttrkrgkgmkkysgrg
ahrvgwrk
>2505555233;clusterid=381
MTTswkkvtavrggasvgsadanardrdadnavkardgtkakhksarhatsanwgramankgaavcankaardadnkvsv
vkasrkskvmakartvkarvaTATATGGASGAVTAVGsarkrddakaaasssgsdrrdaggaksggadvarkaknTA
>2785752443;clusterid=178
MHTKTTRTGTTAGACadkvavtsgsaatgmraatrdrnaggwngdsgtagaskkaagsgamvgassvaagtdvrkynrnk
gkvvnvggatgskchyhrngnarvktvaamkagtgtkvysmnnyswgdmkatdnaaaggyvgkshdtkvdayarasgatv
tgnwgndmkasraagkrgtadgnanagdvaghyvshnaaggkatyaktghaytvamvgnvkTADGRNTrsaakasdsnga
vrmradhmvvsvvskdarykvdgtdmgvkssadaaavadcrmrd
>2633065019;clusterid=454
MATSSTsnacsvsaaavaangdsvgsvkvykrrdrcnadgscgayyvncaagkttsgsvadtdvvysgvavvagtaygar
msTATATTGCTRATAVAAR
>2518035936;clusterid=513
MSMRMNGRYGDGDTTTGACASARGRVHGRNWGTTCCGAGTVGAGMGGGGVADD
>2505554964;clusterid=425
msnvaarrarraanvavvaagtasgvwvaaavsdgrsddgswvshavskvahwvsgavsamGVRCVMVSGTVSGAVGAAT
VGKRGGAYVGSGATAGMATGYWGCSAATTAAAGKSVG
>2549670091;clusterid=321
mkhvrshrvmgmsvsvaGCANNGTGSSMGGSGTDDRTKSTDSSSTSGTACAAAAGVGACavassdkvkcmvvagaacgva
mganyyydyrrskysntarmnddvkadtkvartytvnddkragksktktdkakaasvdsnamnkdtgmrskvaykktadr
asnggtvtadgskmnskvaskvdgysraTG
>2549666778;clusterid=478
MGKVAGTCYKVDGTTGGGATNVKRTVGyykvdkaawkahtadkttgvdmttcsngkyvsgayvdskaddgadkGSGSW
>2505556882;clusterid=458
MRVAGGCAAATTATmmhrradrdwmvrnagrwsmmdgarngwadgnaraamamtsdmhgrytayrgmrrddrwvysanay
trkdgsyrvtndsm
>2556072832;clusterid=270
MGdkkvavggssrdvsasgavarsaghvavdtasggarraskvkvdsdsarsgkssagagvdvahggtgdgtadaggayt
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Hoy 1 de abril del 2024
Ahora se ejecutara este comando, para analizar las secuencias
```
vsearch --cluster_fast DATA_FAA/fromscriptall.genes.faa --id 0.6 --centroids ./RESULTADOS/PRUEBAS2/centroidsrPseudo.faa --clusterout_id --clusterout_sort --consout ./RESULTADOS/PRUEBAS2/consoutPseudoPrueba2.consout --msaout ./RESULTADOS/PRUEBAS2/msaoutPseudoPrueba2.msout --uc ./RESULTADOS/PRUEBAS2/UCPseudoPrueba2.uc
```

Resultados
```
==> UCPseudoPrueba2.uc <==
S       0       4856    *       *       *       *       *       2785749539      *
S       1       4480    *       *       *       *       *       2972001972      *
S       2       4271    *       *       *       *       *       2518032096      *
H       2       4239    73.1    +       0       0       13D150M6D213M7D241MD44M2D237M3D619M6I118M2D213MI68MI104M4I694MI69MD157M6I71M9I114M5I245M5I266M4I142M11I272M3I167M11I      2549670384      2518032096
H       2       4203    75.8    +       0       0       15D54M2D59M8I522MD748M3D269M17I164M2I120M4D335M5I145M3I94M5I54M12I253M6I42MD334M2I452M3I142M5I293M4I97M22I        2633066195      2518032096
H       2       4150    73.3    +       0       0       28D256MI91M2D48M8I287M2D346M7I291M4I106M4I14M4I110M6I241M2I68M9I73M9I207M3D104M22I219M2I127M3I27M7I113M3D94M4I168M2I353MI127M9I69MI252M7I250M2I71M45I     2923166973      2518032096
S       3       4029    *       *       *       *       *       2923170970      *
H       3       3665    69.4    +       0       0       136I116M5I214M9I92MD249M4I182M2D78MD89M2I147M3I180MD22M6I156M9D397M9I86M2I45M2I67M6I264M6I254MI353MI190MD144M6I63M6I159M3I103M172I        2714614382      2923170970
H       3       3657    69.0    +       0       0       265I220M8I394M4I181MD42M5D393M2I267M3D89MD431M7I165MD112M9I155M5I193MD87M8I195M14I122M2I366M4D71MI158M63I 2549668513      2923170970
H       3       3468    70.7    +       0       0       500I234M2I121MD174M7I146M3I90M2I189MD66M2I68M9I41M2I105M3I75M2I108M6I42M9I385M2I144M10I284MD148M6I504MI50MI123MD365M2D    2633066528      2923170970
S       4       3296    *       *       *       *       *       2923168233      *
H       4       3182    72.3    +       0       0       37I59M3I288M10I238M6I153MD56M2I25M3I203M2D245M2D49M9I469M8I93MD256M2D414M2I71MI134M3D98M3D87M2I102M2I128M43I      2972007055      2923168233
H       4       3049    70.7    +       0       0       58I171M13I352MI48M5I112M23I196M20I101MD223M3I274M6I271M3I118M8I54MD80M8I92M5I250M2I259M10I36M7I39MI298M2D48M3I23M75I      2556075033      2923168233
H       4       2968    73.0    +       0       0       122I178MD94M3I140M3I193M6I196MI30MI77MI245M3D61M4D584M2I240MI303M8I145M8I38M31I129MI72M14I109M2I126M132I  2714616755      2923168233
H       4       2963    71.2    +       0       0       260I186M4I30M2I65M10I113M2I107M8I169M3I126M2I78M7D248MI128M4I237M16I86M3D135M4I228MI91M16I238M5I156M2D178M3I149M3I203MI   8011073211      2923168233
H       4       2948    70.3    +       0       0       211I227M4D157M2D450M6I155M14I74M4I51M2I253MI111M13I109M9I105M13I160M12I241MD69M4D669MI67M2I39M71I 2972004231      2923168233
S       5       2934    *       *       *       *       *       2972004192      *
S       6       2903    *       *       *       *       *       2556078011      *
H       6       2847    74.4    +       0       0       37I308M3I139M9I172M7I83MI125M9I262MD289MD153M2D105M2I190M4I94MD502M2D239MD170M8D  2923168179      2556078011
S       7       2745    *       *       *       *       *       2518034016      *
H       7       2716    76.6    +       0       0       7I262M3I191MI76M4I363MD121M3D133M2D203MI220MI475MI56M2I176M17I287MI144M3D 2923167232      2518034016
S       8       2712    *       *       *       *       *       8011076232      *
H       8       2709    72.3    +       0       0       7D104M2D116M4I189MI143M2D100M4D239M3D143M3D204M12I255MI161MI40MI586MI55M3D163MD186M7I     2972005190      8011076232
H       8       2624    73.3    +       0       0       55I181M2D119M2I117M2D17M4D51MD195MI62M7D74M2D444M12I138M3I205M15I92MD88M8I98MI78MI312M7I83MD250M3I        2518035654      8011076232
H       8       2619    71.7    +       0       0       42I85M13I116M2D307M3I43M7I98M3D211M5D166M2D143M12I395M3I247MI413M6D377M30I        2556075010      8011076232
H       8       2619    70.9    +       0       0       24I32MD155M2D162M7I50MI222M3I104M4I155MI60M6D835M6D233M3D194M18I61M9I338M44I      8011076810      8011076232
H       8       2593    73.9    +       0       0       86I41M6I363M2I375MD230M2I271MI429M5I196M3D250M4D430M25I 26330681818011076232
H       8       2590    72.5    +       0       0       35I167M10I55M10I248M3I60MI100M13I169M2D119M2D585M3D91M4D279M6I86M2I346M11I206MI68M41I     2505553445      8011076232
H       8       2589    72.4    +       0       0       17I97MI115M3I208M2I105MD369MD32M8I53M3D113M6I258M17I136M10I158M3I91M9I106M4I29MI499M6I215M41I     2549669578      8011076232
H       8       2587    71.6    +       0       0       5I179M5D49MI126M2I74M4D100MI61M7I147M5I227M4I201M5I144M13I400M4I165MI427M3I110M7I168M76I  2972005913      8011076232

==> centroidsrPseudo.faa <==
>2518034652;clusterid=461
MRKTAAAAGCAMTanmawvdstndrvardkrrdgrvsgshvvrdyvnggggsmggttvrcytdyhkagryvarsmamtar
ydakgvavryCM
>2633065095;clusterid=410
vrhwrgsssaasahagntrrraawdsgrrsraraskahgrrdaaahwahvsrsaranagahgwravrdaagrmanasstr
rrkdvasrdramashrvTRAGRWVTNAAGGCCTGGTarhrahasGDKGSV
>2518034247;clusterid=391
MDSRTASATARGGATvaaavhaasdarwvsdssTYVRSGTDGHRVGTKSGKTGSGnysvrgngdvwsndsvgsrdavadt
gknddswksrvgmtdsrkkdarnkandssrdtargdnkvmmrymvyGGSAGAGAGATRGRRKNDRW
>2505554406;clusterid=366
MKTVVTGAAGGGACarrgmaddkrvasgdayvvdtnsagmtysgrdvnnaaavvadtrsvssrnnvatrakrsndarvst
vsggvtsycaskgrgamsgdakgkvgstatdtmrkaggnaasddvarvmdkcrtkssassamnrttrkrgkgmkkysgrg
ahrvgwrk
>2505555233;clusterid=381
MTTswkkvtavrggasvgsadanardrdadnavkardgtkakhksarhatsanwgramankgaavcankaardadnkvsv
vkasrkskvmakartvkarvaTATATGGASGAVTAVGsarkrddakaaasssgsdrrdaggaksggadvarkaknTA
>2785752443;clusterid=178
MHTKTTRTGTTAGACadkvavtsgsaatgmraatrdrnaggwngdsgtagaskkaagsgamvgassvaagtdvrkynrnk
gkvvnvggatgskchyhrngnarvktvaamkagtgtkvysmnnyswgdmkatdnaaaggyvgkshdtkvdayarasgatv
tgnwgndmkasraagkrgtadgnanagdvaghyvshnaaggkatyaktghaytvamvgnvkTADGRNTrsaakasdsnga
vrmradhmvvsvvskdarykvdgtdmgvkssadaaavadcrmrd
>2633065019;clusterid=454
MATSSTsnacsvsaaavaangdsvgsvkvykrrdrcnadgscgayyvncaagkttsgsvadtdvvysgvavvagtaygar
msTATATTGCTRATAVAAR
>2518035936;clusterid=513
MSMRMNGRYGDGDTTTGACASARGRVHGRNWGTTCCGAGTVGAGMGGGGVADD
>2505554964;clusterid=425
msnvaarrarraanvavvaagtasgvwvaaavsdgrsddgswvshavskvahwvsgavsamGVRCVMVSGTVSGAVGAAT
VGKRGGAYVGSGATAGMATGYWGCSAATTAAAGKSVG
>2549670091;clusterid=321

==> consoutPseudoPrueba2.consout <==
>centroid=2518034652;seqs=1014;clusterid=461
AAGAAATAAAAAAAATAGAAAAAAAAAGAAAGAAAAAAAAAGGGGAAGGTTAAAATAAAAAGAAAAGAAAATAAAAAAGA
AAA
>centroid=2633065095;seqs=837;clusterid=410
AAAAAAAAAGATAAAAAAAAGAAAAAAAAAAAGGAAAAAAAAGGAAGAAAAAGAAGAAAAAAAAGAAAAAAATAAAAGAA
AAAAAGAGAAATAAGAAATAAAGGAATGGAAAAAAAAAGA
>centroid=2518034247;seqs=672;clusterid=391
ATAAGGATGAAAGGAAAAAGAAAAAATAAAAGAAGAAAGAAAGATGAGAAAAAGAGAAAAAAAAGAAAAAAATGAAAAAA
AAAAGAAAAAAAAAAAAAGAAAAATAAGAAAAAAAAAAAGGAAGAGAGATAGAAAA
>centroid=2505554406;seqs=607;clusterid=366
AAGGGAAAAAGAAAAAAAAAGAAAAAGTAGAGATAAGAAAAGAAAAAAATAAGAAAAAAAAAAAAAAAAAAAAAAGGATA
AAAAAGAGAAAGAAAGAAGATATAAAAAAGGAAAAAAAAAAGAAAATAAAAAAAAAATTAAAGAGAAAAAGAGAAAA
>centroid=2505555233;seqs=560;clusterid=381
AATAAAGGAAAGAAAAAAGAAAAAAAGGAAGGTGAGAAAAAAATAAAAGAAAAAGGAAAAAAAAAAAAAAAAAAAAAAAG
GGAAAAAATAGAAGATATATGGAAGAATAAGAAAGAAGAAAAAAAAGAAAAAAGGAAAGGAAAAAAAA
>centroid=2785752443;seqs=529;clusterid=178
AGAAAAAAAAAAGAAATGAAAATAAAAAGGAAGAAGTAGAGAAAAGAGAAAGAAAGAAGAAAAAAAAAAGAAAAAGGATG
AAAAAAAAGAAAAATGAAAAAGAGTAAAAAAAAAAGAAGAAAAAAAGGAAGAAAATAAAAAAAAGGATATGAAGAAAAAA
AAAGAAGTAGGGAAAGAAAGAAGAAAAAGGAAAAAATGAAAAAAAAGAAATAAGAATAAAAAAGAAAGAGAAAAAGGGAA
AAAAAAAAAAAGTAAGAAAAAAAAAAAA
>centroid=2633065019;seqs=526;clusterid=454
AAAAAAAAAAAAAAGAAAGAAAAAAAAAAAAAGGAAGAGAAAGAAGATTAGAAAATAAAAAGAAAAAGTAAGAGAATAGA
ATGAAAATAAA
>centroid=2518035936;seqs=502;clusterid=513
AGAAGAGATTTGAAAAAAGAAAGAAAGTTAAGAGTAGAGAGGGGAA
>centroid=2505554964;seqs=490;clusterid=425
AAAAAAAAAAAAAAAGTAAGAAGAAAAGAGAAAAGAAAAAAAAAAAAAGAGAAAAGGAAAAAAAGTAAGAAGAATAGAAG
GAAAGAGATAGAAGGGAGAAAATTAAAGA
>centroid=2549670091;seqs=483;clusterid=321
AAAAAGAAAAAAGAAAAGAAAAAGGAGAAAAAAGAAAAATAGAAAAAAAGAGAGAGAAAAAAAAAAAAGAAGGAAAGAAA

==> msaoutPseudoPrueba2.msout <==

>*2518034652
-----------MRKTAAAAGCAMTanmawvdst--ndrvardkrrdgrvsg-shvvrdyvng-gggsmggttvrcytdyh
kagryva--rsmamtarydakgvavryCM-------------
>2518035292
--------------------mssvnhrttgras--aaaasgcahndgashd-vsgtarsaav-gcsnagtvtstdsgsrg
aadaras--amvsktgsytayrdawydkGRGASDCARG----
>2518035593
--------------mkwvrhgaransdarrtah--grvhsaargaasyvra-taavhdtgav-rtvwtdsdvvgrghvvs
hvgtvga--hghagmstasagdwagmtransa----------
>2518035722
------------------MAKHGTCCGATKKVT--VDNTHSACHCSMCRKW-TGGVVHCSKV-Grasvyssdwargcgcg
thyyrka--ndhavvgdgdwddvkawyCANTKTGAG------
>2518035775
-----------MAGraaravvdmaarkaarghv--ataakarrdywnrggg-vngswvnyrg-tamtrsvwhnndnargt
wayarvg--rkvrydarradkrrdsrrnh-------------
>2518035801
mssdkagh---kagraravannanadtnykard--mdasvaasdksggrsd-rtnsrhagam-addtkyrttsdntvdas
nytnaga--stnskkgvsarG---------------------
>2518035810
------------mrkdrtdgnsnartnaarsvn--stcnrvramgvrvtsa-gdvnvhvskv-shrarvmcymtgddyrv
sardytr--gvanrssakvrykTAANGMTR------------
>2518036393
-----------mayksasarvrrnarhrsaarh--chvaswrdgtvvtdgh-watrrykrms-aamaanrrykvvakrgg
haasnna--asrdtagtdkraaraahaGK-------------
>2518036633
------------mvnsrkagkvtrvkmdstrhm--sadvykamagdvgatv-yrvtaagvvr-hndgghavadgghhdhm
vnvtsvm--dakrrvahgyvdhnvyvrkkk------------
>2518036672
--------------mdkydrmaadngrataarv--nsaavarvakasgvtg-yakvdmskgc-vrashgnayattchrvt
```

15 de abril del 2024
# DESARROLLO PARA SCRIPT MATRIZ
Para este punto ya como se vio antes se tienen las columnas con informacion de relevancia, como lo que es la
1. columna 1: que contiene
    a. (S) centroide sequence
    b. (C) cluster sequence
    c. (H) match sequence con el Centoide sequence
2. columna 2: No cluster o centroide al que corresponde
3. columna 9: id de la proteina que correspondiente
4. columna 10: ide de la proteina a la que hizo match, o si corresponde a la (S o C) entonces queda en *

Hasta este punto, para entender como se van a extraer y manejar los datos
```
grep "S" RESULTADOS/PseudoPrueba.uc
grep "S" RESULTADOS/PseudoPrueba.uc | wc -l
Resultado
525
```
```
grep "C" RESULTADOS/PseudoPrueba.uc | wc -l
Resultado
525
```
```
grep "H" RESULTADOS/PseudoPrueba.uc | wc -l
Resultado
55175
```
El codigo siguiente es para entender si se refiere a la columna dos como el numero del cluster
```
grep "C" RESULTADOS/PseudoPrueba.uc | cut -f 2 | head -n 10
Resultado
461
410
391
366
381
178
454
513
425
321
```
Con este otro lo confirmamos, solo queda definir cual va a ser si (S) o (C) los que dicten si es la secuencia representate para la matriz, que lo mas probable sea (S).
```
grep "S" RESULTADOS/PseudoPrueba.uc | cut -f 2 | head -n 10
Resultado
0
1
2
3
4
5
6
7
8
9

```
```
grep "515" RESULTADOS/PseudoPrueba.uc
Resultado
...
```
Con mas resutados

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/4abfeaf6-b319-4361-bebd-f203ca5b0781)
```
# Lo que son varios comando con el mismo resultado
grep "^515" RESULTADOS/PseudoPrueba.uc
grep "^[515]" RESULTADOS/PseudoPrueba.uc
grep "*[515]" RESULTADOS/PseudoPrueba.uc
grep "*515" RESULTADOS/PseudoPrueba.uc
grep -E "^515" RESULTADOS/PseudoPrueba.uc
grep -E "^[515]" RESULTADOS/PseudoPrueba.uc
grep -E "\[515\]" RESULTADOS/PseudoPrueba.uc
grep -E "^\[515\]" RESULTADOS/PseudoPrueba.uc
grep -E "^1" RESULTADOS/PseudoPrueba.uc
grep -E "\t515" RESULTADOS/PseudoPrueba.uc
grep -E " 515" RESULTADOS/PseudoPrueba.uc
grep -E "[a-zA-Z]\t515" RESULTADOS/PseudoPrueba.uc
grep -E "[a-zA-Z]*\t515" RESULTADOS/PseudoPrueba.uc
grep -E "[A-Z]\t515" RESULTADOS/PseudoPrueba.uc
grep -E "[A-Z]\t" RESULTADOS/PseudoPrueba.uc
Resultado
~ Nada pues
```
```
grep -E "*515" RESULTADOS/PseudoPrueba.uc
Resultado
```
Con mas resultados

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/6ae5ec46-65cc-4c40-b6d9-1675eb81d593)

```
grep -E "1" RESULTADOS/PseudoPrueba.uc
Resultado
```
Con mas resultados antes

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/c0e5b367-b3e5-4232-9dc0-e4f9b62bc6d7)

```
grep -E "1+" RESULTADOS/PseudoPrueba.uc
Resultado
```
Con mas resultados antes

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/a910f3a2-b4a2-433d-a802-7bdbe9e32f99)
```
grep -E "[a-zA-Z]*515" RESULTADOS/PseudoPrueba.uc
grep -E "[A-Z]*515" RESULTADOS/PseudoPrueba.uc
Resultado
```
Con mas resultados antes

![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/bf5d51d6-d236-4b39-963c-73ab949d08a9)

```
grep -E "[A-Z]" RESULTADOS/PseudoPrueba.uc
Resultado
```
Con mas resultados antes
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/09e2703d-1b06-46cc-86b9-2d2076822cd5)

```
grep -E "[A-Z]\s" RESULTADOS/PseudoPrueba.uc
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/5c862f38-a7c1-446b-8273-11126ac9fc0c)

```
grep -E "[A-Z]\s515" RESULTADOS/PseudoPrueba.uc
grep -E "^[A-Z]\s515" RESULTADOS/PseudoPrueba.uc
Resultado
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/d1fecb2c-7c9b-4698-8f90-c59c01010d83)


Con lo siguiente se busca comprobar si son la misma informacion la del C con la de S y si compaginan, las demas columnas sin agregar la primera, entonces si podemos usar la informacion con (S) como la refencia.
```
grep -E "^C" ../RESULTADOS/PseudoPrueba.uc | cut -f 2,3,4,5,6,7,8,9,10 > ../MATRIXVSEARCH/C_comp.txt
grep -E "^S" ../RESULTADOS/PseudoPrueba.uc | cut -f 2,3,4,5,6,7,8,9,10 > ../MATRIXVSEARCH/S_comp.txt

#Toca comparar
diff C_comp.txt S_comp.txt > CS_comp.txt
mv CS_comp.txt CS_diffcomp.txt
Resultado
> 505   59      *       *       *       *       *       2556073553      *
> 506   59      *       *       *       *       *       2972005211      *
> 507   56      *       *       *       *       *       2518032230      *
> 508   56      *       *       *       *       *       2633067652      *
> 509   56      *       *       *       *       *       2972005192      *
> 510   56      *       *       *       *       *       2972005194      *
> 511   56      *       *       *       *       *       2972005551      *
> 512   54      *       *       *       *       *       2972004696      *
> 513   53      *       *       *       *       *       2518035936      *
> 514   50      *       *       *       *       *       2505557391      *
> 515   50      *       *       *       *       *       8011073038      *
> 516   49      *       *       *       *       *       2518035892      *
> 517   48      *       *       *       *       *       2923170748      *
> 518   46      *       *       *       *       *       2972004202      *
> 519   43      *       *       *       *       *       2518033594      *
> 520   43      *       *       *       *       *       2518036416      *
> 521   42      *       *       *       *       *       2714615947      *
> 522   40      *       *       *       *       *       2549669480      *
> 523   38      *       *       *       *       *       2785752907      *
> 524   34      *       *       *       *       *       2505556714      *
```
Si para `diff`
    These format options provide fine-grained control over the output
      of diff, generalizing -D/--ifdef.
    LTYPE is 'old', 'new', or 'unchanged'.  GTYPE is LTYPE or 'changed'.
    GFMT (only) may contain:
      %<  lines from FILE1
      %>  lines from FILE2
      %=  lines common to FILE1 and FILE2
```
grep "<" CS_diffcomp.txt | wc -l
Resultado
525

grep ">" CS_diffcomp.txt | wc -l
Resultado
525
```
```
sort -n C_comp.txt | head -n 10
Resultado
0       1       *       *       *       *       *       2785749539      *
1       2       *       *       *       *       *       2972001972      *
2       4       *       *       *       *       *       2518032096      *
3       4       *       *       *       *       *       2923170970      *
4       6       *       *       *       *       *       2923168233      *
5       2       *       *       *       *       *       2972004192      *
6       2       *       *       *       *       *       2556078011      *
7       2       *       *       *       *       *       2518034016      *
8       14      *       *       *       *       *       8011076232      *
9       6       *       *       *       *       *       2518034444      *
```
Lo guardamos con la nueva configuracion
```
sort -n C_comp.txt > C_comp2.txt && mv C_comp2.txt C_comp.txt
head -n 10 C_comp.txt
Resultado
0       1       *       *       *       *       *       2785749539      *
1       2       *       *       *       *       *       2972001972      *
2       4       *       *       *       *       *       2518032096      *
3       4       *       *       *       *       *       2923170970      *
4       6       *       *       *       *       *       2923168233      *
5       2       *       *       *       *       *       2972004192      *
6       2       *       *       *       *       *       2556078011      *
7       2       *       *       *       *       *       2518034016      *
8       14      *       *       *       *       *       8011076232      *
9       6       *       *       *       *       *       2518034444      *
```
Pero como vimos en base a al orden de columnas de estas nuevas tablas, contienen distintos tipos de numeracion en la columna 2, aun que sean los mismo: vemos que lo id's de las proteinas coinciden con el orden numerico:
```
head -n 10 S_comp.txt
0       4856    *       *       *       *       *       2785749539      *
1       4480    *       *       *       *       *       2972001972      *
2       4271    *       *       *       *       *       2518032096      *
3       4029    *       *       *       *       *       2923170970      *
4       3296    *       *       *       *       *       2923168233      *
5       2934    *       *       *       *       *       2972004192      *
6       2903    *       *       *       *       *       2556078011      *
7       2745    *       *       *       *       *       2518034016      *
8       2712    *       *       *       *       *       8011076232      *
9       2432    *       *       *       *       *       2518034444      *

head -n 10 C_comp.txt
0       1       *       *       *       *       *       2785749539      *
1       2       *       *       *       *       *       2972001972      *
2       4       *       *       *       *       *       2518032096      *
3       4       *       *       *       *       *       2923170970      *
4       6       *       *       *       *       *       2923168233      *
5       2       *       *       *       *       *       2972004192      *
6       2       *       *       *       *       *       2556078011      *
7       2       *       *       *       *       *       2518034016      *
8       14      *       *       *       *       *       8011076232      *
9       6       *       *       *       *       *       2518034444      *
```
Ahora corremos estos comandos para guardar de nueva manera, para finalmente comparar y ver si cambia algo
```
cut -f 1,3,4,5,6,7,8,9 S_comp.txt > S_comp2.txt && mv S_comp2.txt S_comp.txt
cut -f 1,3,4,5,6,7,8,9 C_comp.txt > C_comp2.txt && mv C_comp2.txt C_comp.txt
```
Y como ahora no muestra diferencias, finalmente podemos decir que son lo mismo
```
diff S_comp.txt C_comp.txt
Resultado
Nada jeje
```
Para este punto podemos generar otro archivo y solo trabajar con aquellos que tienen la etiqueta de (S) y (H)

Estas son variables `resultados` que guarda la direccion de resultados en VSEARCH y `code` que guarda la direccion donde se encuentra el script
```
head -n 20 PseudoPrueba.uc | grep -E "[A-Z]\s2"
Resultados
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/f9389908-ccd6-4c5b-ac45-40049789a9c2)

```
head -n 20 PseudoPrueba.uc | grep -E "^[A-Z]\s2"
Resultados
```
![image](https://github.com/Marcos0Ramirez/Pseudomnas_Bitacora/assets/88853577/ae089c3b-5d12-4fce-9734-9aba87930407)

Se guardo la info necesaria, y como sabemos solo se clusterizaron 525.
```
grep -v -E "^C" PseudoPrueba.uc > SH_PseudoPrueba.uc
```
Se guarda el avance necesario
```
#!/bin/bash

# Esta es la direccion donde se aroojaran los resultados para la matriz
GENOMAS="Direccion/Descargas_NCBI/IMGPSEUDOMONASGENOMES"
RESULTADO="Direccion/Descargas_NCBI/VSEARCH/MATRIXVSEARCH"
INPUT="Direccion/Descargas_NCBI/VSEARCH/RESULTADOS"

cd $GENOMAS
totalS=$(grep -E "^S" $INPUT/SH_PseudoPrueba.uc | wc -l)

for ((i=0; i<=$totalS; i++))
do
        cluster=$(grep -E "^[A-Z]\s$i" $INPUT/SH_PseudoPrueba.uc) # Llamada de los datos para ser procesados por correspondencia del numero del cluster.
        while CLUST= read -r lineas; do
                id=$(cut -f 9)
                for j in $id
                do
                        grep -l "$j" */*genes.fna
                        echo "$j"
                done
        done <<< $cluster
done


Resultados
```
```

Resultados
```
```

Resultados
```
```

Resultados
```


