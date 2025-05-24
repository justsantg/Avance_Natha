load "datos.csv";
filter column "fecha_salida" >= "2024-01-01";
filter column "fecha_llegada" <= "2024-06-01";
aggregate count column "id_transporte";
aggregate average column "costo_transporte";
print;
