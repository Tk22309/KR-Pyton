from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def func_give_header(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    Table = soup.find('table', class_="sc-1x32wa2-1 dYkgjk")

    thead = Table.find_all("thead")
    for th in thead:
        cols = th.find_all("th")
        data = [col.get_text(strip=True) for col in cols] 
        with open("C:\\Users\\User\\Desktop\\KR Pyton\\MyText.txt", "w", newline='', encoding='cp1251') as f:
            f.write(";".join(data) +';Дата'+'\n') 

def give_info_for_month(url):
    patern = re.search(r'/(\d{4})-(\d{2})-(\d{2})/', url)
    year = patern.group(1)
    month = patern.group(2)
    day = patern.group(3)
    formatted_date = f"{month}-{year}"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    Table = soup.find('table', class_="sc-1x32wa2-1 dYkgjk")
        
    rows = Table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        data = [col.get_text(strip=True)[:6] for col in cols] 
        with open("C:\\Users\\User\\Desktop\\KR Pyton\\MyText.txt", "a", newline='', encoding='cp1251') as f:
            f.write(";".join(data))  
            f.write(f';{formatted_date}'+'\n')
          
def remove_empty_rows(filename):
    df = pd.read_csv(filename, sep=';', encoding='cp1251')
    df.drop(columns=['Курс НБУ'], inplace=True)
    df = df.dropna(subset=['Валюта'])
    df.to_csv(filename, sep=';', index=False, encoding='cp1251')



year = 2015
month = 1

while True:    
    formatted_year = str(year)
    formatted_month = str(month).zfill(2)
    url = f"https://minfin.com.ua/currency/ukrainka/{formatted_year}-{formatted_month}-01/"
    func_give_header(url)
    break

while True:
    if year <= 2023:
        if month <= 12:
            formatted_year = str(year)
            formatted_month = str(month).zfill(2)

            url = f"https://minfin.com.ua/currency/ukrainka/{formatted_year}-{formatted_month}-01/"

            give_info_for_month(url)

            month += 1
        else:
            year += 1
            month = 1
    else:
        break
        
filename = "C:\\Users\\User\\Desktop\\KR Pyton\\MyText.txt"
remove_empty_rows(filename)

print("Parsing the end")    


