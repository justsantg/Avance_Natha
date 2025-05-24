load "datos.csv";
filter column "origen" == "Cali";
filter column "destino" == "Bogotá";
aggregate average column "costo_transporte";
print;
