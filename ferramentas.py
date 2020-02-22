import os.path
from pathlib import Path

# constante que define o caminho que será usado
BASE_PATH = str(Path.home()) + os.path.sep + 'Desktop' + os.path.sep + 'saida' + os.path.sep 
ENCODING = 'UTF-8' # constante que define a codificação no arquivo

def criausers(variavelTeste): # função basica para criar TXT
    for i in range(variavelTeste):

        if(os.path.isfile(BASE_PATH + r'{}.txt'.format(i))):
            continue
        else:
            file = open(BASE_PATH + r'{}.txt'.format(i), 'w', encoding=ENCODING)
            file.write("Teste de Texto.\nNumber {}\nOrigem: Ferramentas.py".format(i))
            file.close()        
            print("os arquivos foram criados")