load "datos.csv";
filter column "conductor" == "Ana Torres";
aggregate sum column "costo_transporte";
aggregate count column "id_transporte";
print;
