import numpy as np
import matplotlib.pyplot as plt
from leitorarquivo import LeitorArquivo
 
def main():
    
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)
    
    plt.title('Gráfico de linhas')
    
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    
    i = 1
    for serie in valores:
        plt.plot(serie, label='Série ' + str(i))
        i =+ 1
    plt.legend(loc='upper left')
    
    plt.plot(valores)
    plt.show()

main()