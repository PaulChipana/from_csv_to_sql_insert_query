import csv
import os

# Programa para transformar registros de archivos .csv a consultas INSERT INTO STATEMENTS y facilitar carga de registros a MySql databases  

# Reemplace estos valores con su archivo local CSV y el nombre de tabla deseada
# csv_filename = 'YOUR_CSV.csv'
# table_name = 'your_table'

def csv_to_sql_insert(csv_filename, table_name):
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        columns = csv_reader.fieldnames

	# Obtener ruta de carpeta contenedora de "csv_filename"(file A) para que el OUTPUT file (file B) y el csv file de origen (file A) se encuentren en la misma carpeta 
        carpeta_archivo_a = os.path.dirname(csv_filename)
        nombre_archivo_b = "INSERT_SQL_QUERY_OUTPUT.sql" 
        ruta_archivo_b = os.path.join(carpeta_archivo_a, nombre_archivo_b)

        # Crear y Abrir el archivo de salida una sola vez antes del bucle
        with open(ruta_archivo_b, 'w') as output_f:
            for row in csv_reader:
                values = [f"'{row[col]}'" if isinstance(row[col], str) else str(row[col]) for col in columns]

                sql_insert = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(values)});"

                # Escribir cada consulta INSERT en el archivo de salida         
                output_f.write(sql_insert + '\n')
    print('¡Archivo creado exitosamente!')

# REPLACE FIELDS :
# csv_to_sql_insert("csv_filename", 'table_name')

# Ejemplo de uso :
# csv_to_sql_insert(r"C:\Users\GIGABYTE\Documents\Amazon s3 storage\ecommerce_events_history_in_electronic_store.csv",'ecommerce_events_history_in_electronic_store')
    # "r": hemos colocado este caracter antes de comillas, para que python no piense q "\U" es un CARACTER UNICODE
    # Agregar "r" NO sería necesario, si la ruta del archivo (PATH File) usara "/"(slash), en lugar de "\" (backslash)

