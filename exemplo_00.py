from time import sleep

def primeira_atividade():
    print('primeira atividade')

def segunda_atividade():
    print('segunda atividade')

def terceira_atividade():
    print('terceira atividade')

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(1)
