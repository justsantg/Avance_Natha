load "datos.csv";
filter column "conductor" == "Carlos Ruiz";
aggregate count column "id_transporte";
aggregate sum column "costo_transporte";
print;
