from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

def process_csv():
    # Leer el archivo CSV
    df = pd.read_csv(r"C:\Users\cesar\Desktop\platzi\ETL_Workshop_02\DATA_CSV\spotify_dataset.csv")
    # Aquí podrías agregar código para procesar o transformar los datos
    # Por ejemplo, cargarlos en una base de datos
    print(df.head())

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

dag = DAG('procesar_csv',
          default_args=default_args,
          schedule_interval='@daily')

task1 = PythonOperator(
    task_id='leer_y_procesar_csv',
    python_callable=process_csv,
    dag=dag,
)

task1
