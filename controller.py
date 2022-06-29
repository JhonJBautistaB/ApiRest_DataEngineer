import sqlite3
from sqlite3 import Error
from datetime import datetime

def new_connect():
    try:
        db_name = "countrylanguages.db" #variable de entorno
        connection = sqlite3.connect(f"database/{db_name}")
        #cursor = connection.cursor()
        #print("connection established")
        return connection

    except Error as er:
        print('No fue posible conectarse {}'.format(er))

# Inicializar tablas
def init_tb_db():
    sql_create_tb_cl = """CREATE TABLE country_languages (
                            region TEXT,
                            city TEXT,
                            languages TEXT,
                            process_time REAL
                        );"""
    sql_create_tb_et = """CREATE TABLE execution_time (
                            total_time REAL,
                            average_time REAL,
                            min_time REAL,
                            max_time REAL,
                            generation_date TEXT
                        );"""
    conn = new_connect()
    cursor = conn.cursor()
    cursor.execute(sql_create_tb_cl)
    cursor.execute(sql_create_tb_et)
    conn.commit()

def insert_table(t_time_p, t_average_p, min_time_p, max_time_p):
    conn = new_connect()
    cursor = conn.cursor()
    
    date_time_process = datetime.now()

    sql = f"INSERT INTO execution_time (total_time, average_time, min_time, max_time, generation_date) VALUES ({t_time_p},{t_average_p}, {min_time_p}, {max_time_p}, '{date_time_process}');" 
    cursor.execute(sql)
    conn.commit()
    #cursor.close()
    
    
