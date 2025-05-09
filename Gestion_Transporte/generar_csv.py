import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('es_CO')

tipos_carga = ["Líquidos", "Sólidos", "Gases", "Alimentos", "Electrónicos"]
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga"]
empresas = ["TransCarga", "FastCargo", "EnvioYA", "LogiTruck", "CargaExpress"]
estados = ["entregado", "en tránsito", "cancelado"]

with open("datos.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "id_transporte", "tipo_carga", "origen", "destino", "fecha_salida",
        "fecha_llegada", "empresa_transportadora", "costo_transporte",
        "conductor", "estado_entrega"
    ])

    for i in range(1, 301):
        tipo = random.choice(tipos_carga)
        origen, destino = random.sample(ciudades, 2)
        fecha_salida = fake.date_between(start_date='-6M', end_date='today')
        fecha_llegada = fecha_salida + timedelta(days=random.randint(1, 5))
        empresa = random.choice(empresas)
        costo = random.randint(80000, 500000)
        conductor = fake.name()
        estado = random.choice(estados)

        writer.writerow([
            i, tipo, origen, destino,
            fecha_salida.strftime("%Y-%m-%d"),
            fecha_llegada.strftime("%Y-%m-%d"),
            empresa, costo, conductor, estado
        ])
