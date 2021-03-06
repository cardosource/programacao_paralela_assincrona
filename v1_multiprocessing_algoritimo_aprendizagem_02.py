import multiprocessing
from functools import partial
import numpy as np
import datetime

inicio = datetime.datetime.now()

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)


def processar(epocas, entradas,saidas,taxaAprendizagem,momento,pesos0, pesos1,f):
       
    for j in range(epocas):
        camadaEntrada = entradas
        somaSinapse0 = np.dot(camadaEntrada, pesos0)
        camadaOculta = sigmoid(somaSinapse0)
    
        somaSinapse1 = np.dot(camadaOculta, pesos1)
        camadaSaida = sigmoid(somaSinapse1)
    
        erroCamadaSaida = saidas - camadaSaida
        mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
        print(f"Epocas {j}.... Erro: {str(mediaAbsoluta)}")    
        derivadaSaida = sigmoidDerivada(camadaSaida)
        deltaSaida = erroCamadaSaida * derivadaSaida
    
        pesos1Transposta = pesos1.T
        deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
        deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
        
    
        camadaOcultaTransposta = camadaOculta.T
        pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
        pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)
    
        camadaEntradaTransposta = camadaEntrada.T
        pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
        pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)


entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[0],[1],[1],[0]])
pesos0 = 2*np.random.random((2,3)) - 1
pesos1 = 2*np.random.random((3,1)) - 1
epocas=10000
taxaAprendizagem = 0.5
momento = 1

def main():
    iterable =  list(range(1))
    tamanho_pool  = multiprocessing.cpu_count() * 4
    pool = multiprocessing.Pool(processes=tamanho_pool)    
    func = partial(processar, epocas, entradas,saidas,taxaAprendizagem,momento,pesos0, pesos1)
    pool.map(func, iterable)
    pool.close()
    pool.join()

    
    
if __name__ == "__main__":
    main()

tempo_atual = datetime.datetime.now() - inicio
print(f'Tempo de dura????o foi de {tempo_atual.total_seconds():.5f} segundos')
