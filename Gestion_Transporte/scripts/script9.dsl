load "datos.csv";
filter column "empresa_transportadora" == "EnvioYA";
filter column "tipo_carga" == "Gases";
aggregate count column "id_transporte";
aggregate sum column "costo_transporte";
print;
