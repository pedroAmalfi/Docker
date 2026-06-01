import matplotlib.pyplot as plt


def gerar_grafico(df):

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["entrada"],
        df["tempo_ms"],
        marker="o"
    )

    plt.title("Tempo de Execução x Entrada")

    plt.xlabel("Número Sorteado")

    plt.ylabel("Tempo (ms)")

    plt.grid(True)

    plt.savefig("/app/output/performance_graph.png")

    plt.close()
