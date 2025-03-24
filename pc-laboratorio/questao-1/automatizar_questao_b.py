import subprocess
import numpy as np
from scipy.stats import norm
import os
import csv

def executar_algoritmo(algoritmo, t, max_val, repeticoes):
    tempos = []
    caminho_programa = os.path.expanduser("~/downloads/ADS-PRATICA-3/ADS-Lab4/bin")
    for _ in range(repeticoes):
        resultado = subprocess.run([
            "java", "-cp", caminho_programa, "MedidorDeOrdenacao", algoritmo, str(t), str(max_val)
        ], capture_output=True, text=True, cwd=caminho_programa)

        linhas = resultado.stdout.strip().split("\n")
        if len(linhas) > 1:
            dados = linhas[-1].split()
            try:
                tempo = float(dados[-1])
                tempos.append(tempo)
            except ValueError:
                print(f"Erro ao converter saída para float: {dados[-1]}")
        else:
            print(f"Saída inesperada do programa Java: {resultado.stdout.strip()}")

    return np.array(tempos)

def calcular_intervalo_confianca(tempos, confianca=0.95):
    if len(tempos) == 0:
        return float('nan'), float('nan'), float('nan')
    media = np.mean(tempos)
    desvio_padrao = np.std(tempos, ddof=1)
    z = norm.ppf((1 + confianca) / 2)
    erro_padrao = desvio_padrao / np.sqrt(len(tempos))
    intervalo = z * erro_padrao
    return media, media - intervalo, media + intervalo

def main():
    algoritmos = ["quick", "merge", "counting"]
    t = 9400000
    max_val = 940000
    repeticoes = 38 #Usa o número máximo de amostras obtidos anteriormente

    with open("pc-laboratorio/questao-1/resultados/resultado_questao_b.csv", "w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Algoritmo", "TamanhoDaEntrada", "ValorMaximo", "TempoDeOrdenacao"])
        
        for algoritmo in algoritmos:
            print(f"Executando {algoritmo} {repeticoes} vezes...")
            tempos = executar_algoritmo(algoritmo, t, max_val, repeticoes)
            for tempo in tempos:
                escritor.writerow([algoritmo, t, max_val, tempo])

if __name__ == "__main__":
    main()
