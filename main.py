import pandas as pd
import requests
import json
import hashlib
import time
from controller import insert_table, new_connect


# Constante con la URL para extraer los lenguajes de una región for continent
URL_REGION = 'https://restcountries.com/v3.1/region/Africa'

# Array para guardar arreglo de diccionario
data_set_list = []
# 



if __name__ == "__main__":
    # realiza get a la url para traer data
    req = requests.get(URL_REGION)

    if req.status_code == 200:
        # tranformar el request a JSON
        data_json = json.loads(req.text)

        """La respuesta que se recibe de la petición es un array de diccionarios que corresponde
        a cada uno de los paises que componen una región y se itera para obtener los registros deseados
        """        
        for i in range(len(data_json)):
            # inicio tiempo
            start_time_reg = time.time()
            
            # Columnas del dataset
            region = data_json[i].get('region')
            city = data_json[i]['name']['common']   
            # obtener el json de los diferente lenguajes de un pais 
            languages_dic = data_json[i]['languages']
            # obtener los valores del diccionario
            languages = tuple(languages_dic.values())    

            # ciclo para armar set datos requerido            
            for j in range(len(languages)):
                # Hash para nombre del lenguaje
                language = hashlib.sha1()
                language.update((languages[j].encode('utf-8')))

                # tiempo transcurrido
                end_time_reg = time.time()
                
                # Set de Datos requerido
                dataset = {
                    'region': region,
                    'city': city,
                    'languages': language.hexdigest(),
                    'time': (end_time_reg - start_time_reg) # tiempo procesamiento registro
                }
                # Guardar Set diccionario en un array list
                data_set_list.append(dataset)
                # Guardar set de datos en archivo JSON
                with open('data/data.json', 'w') as ds:
                    json.dump(data_set_list, ds)
    else:
        print("no obtuvo ninguna respuesta de la RESTAPI {}".format(req.status_code))


    # Trabajando con PANDAS    
    df = pd.read_json("../tangeloApiRest_prueba/data/data.json")
    # impresión en dataframe JSON data
    with open('data/table.html', 'w') as tb:
        tb.write(str(df.to_html()))

    total_time_process = df['time'].sum()
    total_average_process = df['time'].mean()
    min_time_process = df['time'].min()
    max_time_process = df['time'].max()
    
    # Insertar registros en tabla
    data_insert_df = insert_table(total_time_process, total_average_process, min_time_process, max_time_process)