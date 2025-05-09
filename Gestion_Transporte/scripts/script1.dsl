load "datos.csv";
filter column "estado_entrega" == "entregado";
aggregate count column "id_transporte";
print;
