load "datos.csv";
filter column "origen" == "Bogotá";
filter column "destino" == "Medellín";
aggregate count column "id_transporte";
print;
