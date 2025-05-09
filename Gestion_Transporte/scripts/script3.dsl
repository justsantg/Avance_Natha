load "datos.csv";
filter column "empresa_transportadora" == "TransCarga";
aggregate sum column "costo_transporte";
aggregate count column "id_transporte";
print;
