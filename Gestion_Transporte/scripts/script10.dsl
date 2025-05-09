load "datos.csv";
filter column "destino" == "Cali";
aggregate count column "id_transporte";
aggregate average column "costo_transporte";
print;
