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
        return float('nan'), float('nan'), float('nan'), float('nan')
    media = np.mean(tempos)
    desvio_padrao = np.std(tempos, ddof=1)
    z = norm.ppf((1 + confianca) / 2)
    erro_padrao = desvio_padrao / np.sqrt(len(tempos))
    intervalo = z * erro_padrao
    return media, media - intervalo, media + intervalo, erro_padrao

def main():
    algoritmos = ["quick", "merge", "counting"]
    tamanho_entrada = 9400000  # Mantemos fixo em 9,4 milhões
    valores_maximos = [940000, 94000000]  # Testamos com 940 mil e 94 milhões
    repeticoes = 3
    margem_erro_max = 0.02  # Margem de erro de 2%

    with open("notebook-pessoal/questao-2/resultados/resultado_questao_b.csv", "w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Algoritmo", "TamanhoDaEntrada", "ValorMaximo", "TempoDeOrdenacao", "IntervaloInferior", "IntervaloSuperior", "ErroPadrao"])

        for max_val in valores_maximos:
            print(f"Analisando valor máximo {max_val}...")
            resultados_algoritmos = []

            for algoritmo in algoritmos:
                tempos = executar_algoritmo(algoritmo, tamanho_entrada, max_val, repeticoes)
                media, intervalo_inferior, intervalo_superior, erro_padrao = calcular_intervalo_confianca(tempos)

                # Garantir que a margem de erro seja <= 2%
                if erro_padrao / media <= margem_erro_max:
                    print(f"Algoritmo {algoritmo} com valor máximo {max_val}: OK (Margem de erro dentro do limite).")
                else:
                    print(f"Algoritmo {algoritmo} com valor máximo {max_val}: ALTO erro ({erro_padrao / media:.4f})")

                escritor.writerow([algoritmo, tamanho_entrada, max_val, media, intervalo_inferior, intervalo_superior, erro_padrao])
                resultados_algoritmos.append((algoritmo, media, intervalo_inferior, intervalo_superior))

            # Determinar o melhor e pior algoritmo para esse valor máximo
            resultados_algoritmos.sort(key=lambda x: x[1])  # Ordenar pelo tempo médio
            melhor_algoritmo = resultados_algoritmos[0]
            pior_algoritmo = resultados_algoritmos[-1]

            print(f"Melhor algoritmo para valor máximo {max_val}: {melhor_algoritmo[0]} com tempo médio {melhor_algoritmo[1]:.4f} segundos.")
            print(f"Pior algoritmo para valor máximo {max_val}: {pior_algoritmo[0]} com tempo médio {pior_algoritmo[1]:.4f} segundos.")

if __name__ == "__main__":
    main()
