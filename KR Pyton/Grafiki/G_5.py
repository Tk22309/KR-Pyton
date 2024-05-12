import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

valuta = 'USD'

df = pd.read_csv("C:\\Users\\User\\Desktop\\KR Pyton\\MyText.txt", delimiter=';', encoding='cp1251')

valuta_data = df[df['Валюта'] == valuta].copy() 
valuta_data['Рік'] = valuta_data['Дата'].apply(lambda x: int(x.split('-')[1]))

valuta_data['Покупка'] = valuta_data['Покупка'].str.replace(',', '.').astype(float)
valuta_data['Продажа'] = valuta_data['Продажа'].str.replace(',', '.').astype(float)

sns.set_theme(style="whitegrid")
sns.lmplot(data=valuta_data, x='Рік', y='Покупка', palette='tab10')
plt.xlabel('Період')
plt.ylabel(f'Ціна {valuta} в UAN')
plt.title(f'Середня річна ціна {valuta} у проміжку з 2015 по 2023 рік')
plt.xticks(rotation=0)

plt.show()
