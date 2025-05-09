load "datos.csv";
filter column "estado_entrega" != "cancelado";
aggregate average column "costo_transporte";
print;
