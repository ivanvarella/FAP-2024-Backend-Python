import pandas as pd
import matplotlib.pyplot as plt
import os

caminho_base = os.getcwd()
caminho_projeto = os.path.join(
    caminho_base,
    "Modulo3",
    "atividades",
    "Teste1_mod3_preparation",
    "semana7",
    "exercicio1",
)
caminho_arquivo = os.path.join(caminho_projeto, "dados.csv")

# Passo 1: Carregar o conjunto de dados
df = pd.read_csv(caminho_arquivo)

# Passo 2: Limpar os dados
print(f"Número de linhas antes da limpeza: {len(df)}")

# Verificar e remover linhas com valores NaN
df = df.dropna()
print(f"Número de linhas após remover NaN: {len(df)}")

# Converter a coluna 'Idade' para numérico
df["Idade"] = pd.to_numeric(df["Idade"], errors="coerce")

# Remover linhas onde 'Idade' se tornou NaN após a conversão
df = df.dropna(subset=["Idade"])
print(f"Número de linhas após converter e limpar 'Idade': {len(df)}")

# Passo 3: Realizar análises básicas
print("\nAnálise da coluna Idade:")
print(f"Média: {df['Idade'].mean():.2f}")
print(f"Mediana: {df['Idade'].median():.2f}")
print(f"Moda: {df['Idade'].mode().values[0]}")

# Passo 4: Visualizar os resultados
plt.figure(figsize=(12, 6))

# Histograma de Idade
plt.subplot(1, 2, 1)
df["Idade"].hist(bins=20)
plt.title("Distribuição de Idade")
plt.xlabel("Idade")
plt.ylabel("Frequência")

# Gráfico de barras para Departamentos
plt.subplot(1, 2, 2)
df["Departamento"].value_counts().plot(kind="bar")
plt.title("Distribuição por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Contagem")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()

# Boxplot para Idade
plt.figure(figsize=(10, 6))
df.boxplot(column=["Idade"])
plt.title("Distribuição de Idade")
plt.ylabel("Idade")
plt.show()

# Análise adicional: Idade média por departamento
idade_media_por_departamento = (
    df.groupby("Departamento")["Idade"].mean().sort_values(ascending=False)
)
print("\nIdade média por departamento:")
print(idade_media_por_departamento)

# Visualização da idade média por departamento
plt.figure(figsize=(12, 6))
idade_media_por_departamento.plot(kind="bar")
plt.title("Idade Média por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Idade Média")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
