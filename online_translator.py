import pandas as pd 
import time
from bs4 import BeautifulSoup
import requests
import sys

file_name = sys.argv[1]
df = pd.read_csv(file_name)
df['translated']=''
df['explanation']=''

for i in range(len(df)):
    wo_word = str(df.iloc[i]['title'])
    if len(wo_word.split(" "))>1:
        wo_word = '%20'.join(wo_word.split(" "))
    page_link = 'https://en.glosbe.com/wo/en/' + wo_word
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, 'html.parser')
    alert = [i.text for i in soup.findAll('p',attrs={"class":"alert alert-info"})]
    if len(alert) != 0:
        df.at[i,'translated'] = '--unk--'
    else:
        df.at[i,'translated']  = [i.text for i in soup.find_all('strong')[1:]]
        df.at[i,'explanation']  = [i.text for i in soup.findAll('div',attrs={"class":"phraseMeaning show-user-name-listener"})]
    time.sleep(3)

df.to_csv('translated_v0.csv',encoding='utf-8', index=False)



