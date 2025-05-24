load "datos.csv";
filter column "tipo_carga" == "Electrónicos";
filter column "estado_entrega" == "entregado";
aggregate average column "costo_transporte";
print;
