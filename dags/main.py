from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2024, 12, 13),
    schedule="* * * * *",
    catchup=False,
) as dag:

    @task
    def helloworld():
        print("Hello World")

    helloworld()
