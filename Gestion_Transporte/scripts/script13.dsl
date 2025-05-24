load "datos.csv";
filter column "fecha_llegada" <= "2024-05-01";
aggregate sum column "costo_transporte";
aggregate count column "id_transporte";
print;
