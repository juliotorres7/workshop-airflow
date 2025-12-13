from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloworld():
    print("Hellow World")

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2925,12,13),
         schedule_interval="* * * * *",
         catchup=False) as dag:
    
    task1 = (function) task_id: Literal['hello_world']
            task_id="hello_world",
            python_callable=helloworld