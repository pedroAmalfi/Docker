import random
import json
import pandas as pd

from metrics import executar_medicao
from graph_generator import gerar_grafico

resultados = []

numeros_sorteados = [random.randint(1, 100) for _ in range(10)]

for numero in numeros_sorteados:

    resultado = executar_medicao(numero)

    resultados.append(resultado)

df = pd.DataFrame(resultados)

df.to_csv("/app/output/metrics.csv", index=False)

resumo = {
    "tempo_medio_ms": round(df["tempo_ms"].mean(), 4),
    "memoria_media_mb": round(df["memoria_mb"].mean(), 4),
    "iteracoes_media": round(df["iteracoes"].mean(), 2)
}

with open("/app/output/metrics.json", "w") as arquivo:
    json.dump(resumo, arquivo, indent=4)

gerar_grafico(df)

print("Execução concluída.")
