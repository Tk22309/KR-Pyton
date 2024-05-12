import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\User\\Desktop\\KR Pyton\\MyText.txt", delimiter=';', encoding='cp1251')

data['Дата'] = pd.to_datetime(data['Дата'], format='%m-%Y')

data['Покупка'] = data['Покупка'].str.replace(',', '.').astype(float)
data['Продажа'] = data['Продажа'].str.replace(',', '.').astype(float)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Дата', y='Покупка', hue='Валюта', palette='tab10', linewidth=2.5)
plt.title('Курс валют')
plt.xlabel('Період')
plt.ylabel('Курс покупки валют у UAN')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
