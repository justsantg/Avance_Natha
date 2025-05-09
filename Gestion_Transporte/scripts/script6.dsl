load "datos.csv";
filter column "fecha_salida" >= "2024-01-01";
filter column "fecha_salida" <= "2024-03-31";
aggregate sum column "costo_transporte";
print;
