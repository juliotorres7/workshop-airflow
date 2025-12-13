from time import sleep
from airflow.decorators import dag
from datetime import datetime

@dag(
        dag_id="minha_segunda_dag",
        description="minha etl braba",
        schedule="* * * * *"
        start_date=datetime(2025,12,13),
        catchup=False
)

def pipeline():

    def primeira_atividade():
        print('primeira atividade')

    def segunda_atividade():
        print('segunda atividade')

    def terceira_atividade():
        print('terceira atividade')

    def quarta_atividade():
        print('pipeline finalizou')

    def pipeline():
        primeira_atividade()
        segunda_atividade()
        terceira_atividade()
        quarta_atividade()
