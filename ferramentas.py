enc = 'UTF-8'
import os.path

def criausers(variavelTeste): # função basica para criar TXT
    for i in range(variavelTeste):
        while os.path.exists(r'C:\Users\danie\Desktop\saida\{}.txt'.format(i)):
            i += 1
        file = open(r'C:\Users\danie\Desktop\saida\{}.txt'.format(i),'w',encoding=enc)
        file.write("Teste de Texto.\nNumber {}\nOrigem: Ferramentas.py".format(i))
        file.close()
    print("os arquivos foram criados")

