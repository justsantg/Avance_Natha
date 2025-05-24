load "datos.csv";
filter column "tipo_carga" == "Sólidos";
filter column "origen" == "Bucaramanga";
aggregate sum column "costo_transporte";
print;
