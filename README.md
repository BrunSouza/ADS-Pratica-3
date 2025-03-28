# Avaliação de desempenho de sistemas

Professor:  [Marcus Carvalho](https://github.com/marcuswac) <br>

Aluno: [Bruno Souza](https://github.com/BrunSouza)

## Descrição 
Projeto feito afim de gerar algoritmos de automação, gráficos e análises para responder a Atividade Prática 3 - Intervalo de confiança.

## Instalação das Dependências
Para executar os scripts corretamente, instale as bibliotecas Python necessárias utilizando o arquivo `requirements.txt`. Execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto
O projeto está organizado da seguinte forma:

```
📂 ADS-Lab4/ #Programa que implementa os algoritmos de ordenação
|
📂 pc-laboratorio/
  ├── 📂 questao-1/
  │   ├── 📂 resultados/ # Contém os datasets gerados
  │   ├── 📂 graficos/    # Contém os gráficos gerados
  │   ├── analises.ipynb  # Notebook de análise dos resultados
  │   ├── automatizar_questao_a.py  # Código de automação para gerar dataset
  └── ...
  ├── 📂 questao-2/
  │   ├── 📂 resultados/  
  │   ├── 📂 graficos/    
  │   ├── analises.ipynb  
  │   ├── automatizar_questao_a.py  
  └── ...
```

## Descrição das Pastas
- **`ADS-Lab4/`**: Contém o código java responsável por implementar os algoritmos de ordenação.
- **`pc-laboratorio/`**: Contém os códigos, datasets, gráficos gerados para responder à atividade.
- **`questao-1/ ou questao-2/`**: Contém o gráficos e datasets, além de arquivo *analises.ipynb*.
- **`resultados/`**: Armazena os datasets gerados para cada questão.
- **`graficos/`**: Contém os gráficos gerados com base nos resultados.

## Execução dos Scripts
Para rodar os scripts de automação, utilize os comandos:

```bash
python pc-laboratorio/questao-1/automatizar_questao_a.py
python pc-laboratorio/questao-1/automatizar_questao_b.py
python pc-laboratorio/questao-2/automatizar_questao_a.py
python pc-laboratorio/questao-2/automatizar_questao_b.py
```

Os resultados gerados serão salvos automaticamente nas pastas `resultados/`
