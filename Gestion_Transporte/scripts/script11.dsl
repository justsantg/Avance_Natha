load "datos.csv";
filter column "costo_transporte" >= 300000;
aggregate count column "id_transporte";
print;
