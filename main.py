import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados de um arquivo CSV
df = pd.read_csv('dados.csv')

# Criar um gráfico de linha
plt.plot(df['Data'], df['Valor'])

# Adicionar títulos e rótulos
plt.title('Dados de exemplo')
plt.xlabel('Data')
plt.ylabel('Valor')

# Exibir o gráfico
plt.show()
