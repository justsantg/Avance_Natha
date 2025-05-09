load "datos.csv";
filter column "tipo_carga" == "Líquidos";
aggregate average column "costo_transporte";
print;
