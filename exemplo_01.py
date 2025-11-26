from time import sleep

from loguru import logger

logger.add("execution.log", format="{time} - {message}", level="INFO", rotation= "1 day")

def primeira_atividade():
    logger.info('primeira atividade')

def segunda_atividade():
    logger.info('segunda atividade')

def terceira_atividade():
    logger.info('terceira atividade')

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(1)
