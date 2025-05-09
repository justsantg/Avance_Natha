load "datos.csv";
filter column "costo_transporte" > 100000;
filter column "estado_entrega" == "entregado";
aggregate average column "costo_transporte";
print;
