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
    return media, media - intervalo, media + intervalo, erro_padrao

def main():
    algoritmos = ["quick", "merge", "counting"]
    tamanhos_entrada = [9400000, 94000000]  # Dois tamanhos de entrada diferentes
    max_val = 940000
    repeticoes = 30
    margem_erro_max = 0.02  # Margem de erro de 2%

    with open("pc-laboratorio/questao-2/resultados/resultado_questao_a.csv", "w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Algoritmo", "TamanhoDaEntrada", "ValorMaximo", "TempoDeOrdenacao", "IntervaloInferior", "IntervaloSuperior", "ErroPadrao"])

        for t in tamanhos_entrada:
            print(f"Analisando tamanho de entrada {t}...")
            for algoritmo in algoritmos:
                tempos = executar_algoritmo(algoritmo, t, max_val, repeticoes)
                media, intervalo_inferior, intervalo_superior, erro_padrao = calcular_intervalo_confianca(tempos)

                # Verificar se a margem de erro é menor ou igual a 2%
                if erro_padrao / media <= margem_erro_max:
                    print(f"Algoritmo {algoritmo} com tamanho {t}: OK (Margem de erro dentro do limite).")
                else:
                    print(f"Algoritmo {algoritmo} com tamanho {t}: ALTO erro ({erro_padrao / media:.4f})")

                # Escrever no arquivo CSV
                escritor.writerow([algoritmo, t, max_val, media, intervalo_inferior, intervalo_superior, erro_padrao])

            # Analisar o melhor e pior algoritmo com base nos intervalos de confiança
            print(f"Analisando os algoritmos para o tamanho de entrada {t}...")
            resultados_algoritmos = []
            for algoritmo in algoritmos:
                tempos = executar_algoritmo(algoritmo, t, max_val, repeticoes)
                media, intervalo_inferior, intervalo_superior, erro_padrao = calcular_intervalo_confianca(tempos)
                resultados_algoritmos.append((algoritmo, media, intervalo_inferior, intervalo_superior))

            # Ordenar os algoritmos pelo tempo médio de ordenação
            resultados_algoritmos.sort(key=lambda x: x[1])  # Ordena pelo tempo médio

            melhor_algoritmo = resultados_algoritmos[0]
            pior_algoritmo = resultados_algoritmos[-1]

            print(f"Melhor algoritmo para tamanho {t}: {melhor_algoritmo[0]} com tempo médio {melhor_algoritmo[1]:.4f} segundos.")
            print(f"Pior algoritmo para tamanho {t}: {pior_algoritmo[0]} com tempo médio {pior_algoritmo[1]:.4f} segundos.")

if __name__ == "__main__":
    main()
