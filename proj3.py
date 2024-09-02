import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame
data = {
    'Gênero': ['Sertanejo', 'Pop', 'Funk', 'MPB', 'Rock', 'Forró', 'Rap', 'Reggae', 'Axé', 'Eletrônica'],
    'Ouvintes (milhões)': [35, 28, 25, 20, 18, 15, 12, 10, 8, 5]
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print(df)

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['Gênero'], df['Ouvintes (milhões)'], color='skyblue')
plt.xlabel('Gênero')
plt.ylabel('Ouvintes (milhões)')
plt.title('Ouvintes por Gênero Musical')
plt.show()

# Gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(df['Ouvintes (milhões)'], labels=df['Gênero'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Proporção de Ouvintes por Gênero Musical')
plt.show()