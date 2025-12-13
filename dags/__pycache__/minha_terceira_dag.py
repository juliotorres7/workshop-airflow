from time import sleep
from airflow.decorators import dag, task
from datetime import datetime

@dag(
        dag_id="minha_segunda_dag",
        description="minha etl braba",
        schedule="* * * * *",
        start_date=datetime(2024,12,13),
        catchup=False
)

def pipeline():
    @task
    def primeira_atividade():
        print('primeira atividade')
    @task
    def segunda_atividade():
        print('segunda atividade')
    @task
    def terceira_atividade():
        print('terceira atividade')
    @task
    def quarta_atividade():
        print('pipeline finalizou')

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4
