import csv
def actualiza_archivo(NP,RI):
    archivo = "datos.csv" 
    with open(archivo, "w") as archivo_resultados:
        lector_csv = csv.DictReader(archivo_resultados)
        for fila in lector_csv:
            nota_presentacion = fila['nota_presentacion']
            asistencia = fila['asistencia']



with open('datos', 'w') as archivo_resulatdos: 
