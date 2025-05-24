load "datos.csv";
filter column "empresa_transportadora" == "LogiTruck";
filter column "tipo_carga" == "Alimentos";
aggregate count column "id_transporte";
print;
