# FATEC - Laboratório de Análise de Desempenho de Algoritmos com Docker

Repositório Oficial:

https://github.com/pedroAmalfi/Docker


# O que é Docker?

O Docker é uma plataforma que permite executar aplicações dentro de ambientes isolados chamados **containers**.

Um container pode ser imaginado como uma "caixa" que contém tudo o que uma aplicação precisa para funcionar:

* Código-fonte
* Bibliotecas
* Dependências
* Configurações
* Sistema operacional básico

Dessa forma, a aplicação funciona da mesma maneira em qualquer computador que possua o Docker instalado.

---

# Por que utilizar Docker?

Durante o desenvolvimento de software é comum ocorrer a seguinte situação:

> "Na minha máquina funciona, mas na sua não."

Isso acontece porque cada computador possui configurações diferentes, versões diferentes de programas e bibliotecas instaladas.

O Docker resolve esse problema criando um ambiente padronizado para todos os usuários.

Assim, todos os alunos utilizarão exatamente o mesmo ambiente de execução.

---

# O que é um Container?

Um container é uma instância em execução de uma aplicação.

Podemos imaginar:

* Computador = Casa
* Docker = Condomínio
* Container = Apartamento

Cada apartamento possui seus próprios recursos e funciona de forma independente dos demais.

Da mesma forma, cada container executa sua aplicação de forma isolada.

---

# O que é uma Imagem?

Uma imagem Docker funciona como uma receita ou modelo para criar containers.

Por exemplo:

* Imagem Python
* Imagem Ubuntu
* Imagem PostgreSQL

Quando executamos uma imagem, o Docker cria um container baseado nela.

---

# Como o Docker será utilizado neste projeto?

Neste laboratório utilizaremos o Docker para executar uma aplicação Python sem a necessidade de instalar:

* Python
* Pandas
* Matplotlib
* Psutil

Todas essas dependências já estão configuradas dentro do container.

O aluno precisará apenas:

1. Clonar o repositório;
2. Executar o Docker;
3. Rodar o projeto.

---

# Fluxo de Execução do Projeto

O funcionamento deste laboratório ocorre da seguinte forma:

```text
Aluno
   │
   ▼
Git Clone
   │
   ▼
Docker Compose
   │
   ▼
Criação do Container
   │
   ▼
Execução do Python
   │
   ▼
Coleta de Métricas
   │
   ▼
Geração dos Arquivos
   │
   ├── metrics.csv
   ├── metrics.json
   ├── performance_graph.png
   └── iterations_graph.png
```

---

# Vantagens do Docker

Utilizando Docker conseguimos:

* Padronizar o ambiente de execução;
* Evitar problemas de instalação;
* Facilitar a distribuição do projeto;
* Reproduzir experimentos de forma consistente;
* Aproximar o desenvolvimento do ambiente utilizado pelas empresas.

---

# Objetivo deste Laboratório

Além de aprender conceitos de análise de algoritmos e métricas de desempenho, os alunos terão contato com uma das tecnologias mais utilizadas atualmente em:

* Desenvolvimento de Software;
* DevOps;
* Computação em Nuvem (Cloud Computing);
* Integração e Entrega Contínua (CI/CD);
* Engenharia de Software.


## Objetivo

Este projeto tem como objetivo demonstrar a utilização do Docker para execução de aplicações Python, coleta de métricas de desempenho e geração automática de gráficos para análise de algoritmos.

O programa executa um algoritmo simples que:

1. Sorteia 10 números aleatórios entre 100 e 1000;
2. Para cada número sorteado, encontra o N-ésimo número primo correspondente;
3. Mede métricas de desempenho;
4. Salva os resultados em arquivos CSV e JSON;
5. Gera gráficos automaticamente.

Posteriormente, os alunos poderão substituir este algoritmo pelos algoritmos desenvolvidos em sala de aula, como:

* Dijkstra
* A*
* Mochila
* Caixeiro Viajante
* Menor Caminho
* Busca em Grafos
* Outros algoritmos

---

# Pré-requisitos

Antes de iniciar, certifique-se de possuir:

* Git instalado
* Docker Desktop instalado

---

# Testando o Docker

Antes de utilizar este projeto, verifique se o Docker está funcionando corretamente.

Abra um terminal e execute:

```bash
docker run hello-world
```

Se a mensagem de sucesso for exibida, seu ambiente está pronto.

Após executar:

```bash
docker run hello-world
```

você pode verificar se o Docker está ativo utilizando:

```bash
docker ps
```

Se nenhum erro for exibido, seu ambiente está pronto para executar o projeto.

---

# Clonando o Repositório

Execute o comando abaixo:

```bash
git clone https://github.com/pedroAmalfi/Docker.git
```

Entre na pasta:

```bash
cd Docker
```

Caso tenha baixado o projeto em formato ZIP pelo GitHub, descompacte o arquivo e entre na pasta:

```bash
cd Docker-main
```

---

# Estrutura do Projeto

```text
Docker/
│
├── app/
│   ├── main.py
│   ├── metrics.py
│   ├── graph_generator.py
│   └── requirements.txt
│
├── output/
│   └── .gitkeep
│
├── scripts/
│   ├── start.sh
│   └── start.bat
│
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# Executando o Projeto

## Windows

Execute:

```cmd
scripts\start.bat
```

ou

```cmd
docker compose up --build
```
Como na imagem abaixo:
 - ![Executando o comando](https://github.com/pedroAmalfi/Docker/blob/main/imagens/executar.PNG?raw=true)

 Ao executar será inicializado o container e a instalação de suas dependências e, se tudo der certo, aparecerá uma imagem como abaixo:
  - ![Comando Finalizado](https://github.com/pedroAmalfi/Docker/blob/main/imagens/Fim_execucao.PNG?raw=true)

Podem ver no Docker Desktop que existem dois container (hello_word e docker) como imagem abaixo:

  - ![Containers Criados](https://github.com/pedroAmalfi/Docker/blob/main/imagens/Img_Docker.PNG?raw=true)
---

## Linux / MacOS

Execute:

```bash
chmod +x scripts/start.sh
./scripts/start.sh
```

ou

```bash
docker compose up --build
```

---

# O que acontece durante a execução

O sistema irá:

1. Gerar números aleatórios;
2. Encontrar o N-ésimo número primo correspondente;
3. Coletar métricas de desempenho;
4. Gerar arquivos de saída.

---

# Métricas Coletadas

O projeto registra:

| Métrica           | Descrição                                            |
| ----------------- | ---------------------------------------------------- |
| Tempo de Execução | Tempo gasto para processar cada entrada              |
| Memória Utilizada | Diferença observada durante a execução               |
| Iterações         | Quantidade de verificações realizadas pelo algoritmo |

---

# Arquivos Gerados

Após a execução, os resultados estarão na pasta:

```text
output/
│
├── metrics.csv
├── metrics.json
├── performance_graph.png
└── iterations_graph.png
```

---

## metrics.csv

Contém os dados detalhados de cada execução.

Exemplo:

```csv
entrada,primo,tempo_ms,memoria_mb,iteracoes
120,659,1.23,0.00,658
340,2287,8.41,0.00,2286
785,5987,31.55,0.00,5986
```

---

## metrics.json

Resumo estatístico da execução.

Exemplo:

```json
{
    "numeros_sorteados": [120, 340, 785],
    "tempo_medio_ms": 13.73,
    "memoria_media_mb": 0.00,
    "iteracoes_media": 2976.67
}
```

---

## performance_graph.png

Gráfico gerado automaticamente mostrando a relação entre:

* Entrada
* Tempo de Execução

Este gráfico permite visualizar como o tempo de processamento tende a aumentar conforme cresce o tamanho da entrada.

Como pode ser visto na imagem abaixo:

- ![Dados de Saída](https://github.com/pedroAmalfi/Docker/blob/main/imagens/Saida.PNG?raw=true)

---

## iterations_graph.png

Gráfico gerado automaticamente mostrando a relação entre:

* Entrada
* Quantidade de Iterações

Este gráfico é especialmente útil para visualizar o crescimento do esforço computacional do algoritmo independentemente do hardware utilizado.

---

# Como Interpretar os Resultados

Observe que:

* Entradas maiores exigem mais processamento;
* O tempo de execução tende a aumentar;
* O número de operações cresce;
* O consumo de recursos pode aumentar.

Essas informações ajudam a compreender o comportamento dos algoritmos.

---

# Personalizando para o seu Projeto

O algoritmo principal está localizado em:

```text
app/main.py
```

Você pode substituir a função:

```python
encontrar_n_esimo_primo()
```

por qualquer algoritmo desenvolvido na disciplina.

Exemplos:

* Dijkstra
* A*
* Mochila
* Caixeiro Viajante
* Busca em Largura
* Busca em Profundidade

Toda a infraestrutura de métricas continuará funcionando automaticamente.

---

# Limpando os Containers

Caso necessário:

```bash
docker compose down
```

---

# Recriando o Ambiente

```bash
docker compose up --build
```

---

