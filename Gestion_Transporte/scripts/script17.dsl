load "datos.csv";
filter column "estado_entrega" == "en tránsito";
filter column "fecha_salida" >= "2024-01-01";
aggregate count column "id_transporte";
print;
