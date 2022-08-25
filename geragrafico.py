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
    for serie in valores:
        plt.plot(serie)

    plt.show()

main()