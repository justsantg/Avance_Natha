load "datos.csv";
filter column "empresa_transportadora" == "CargaExpress";
filter column "estado_entrega" != "cancelado";
aggregate average column "costo_transporte";
print;
