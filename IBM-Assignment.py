#!/usr/bin/env python
# coding: utf-8

# ### Question 1: Extracting Tesla Stock Data Using yfinance

# In[1]:


pip install yfinance


# In[249]:


import pandas as pd
from matplotlib import pyplot as plt


# In[260]:


import yfinance as yf

ticker_symbol = "TSLA"

tesla_data = yf.Ticker(ticker_symbol)


# In[261]:


tesla_data = pd.DataFrame(tesla_data.history(period="max"))
tesla_data.reset_index(inplace=True)


# In[262]:


tesla_data.head()


# 

# ### Question 2: Extracting Tesla Revenue Data Using Web Scraping
# 

# In[3]:


pip install beautifulsoup4 requests


# In[269]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text

soup = BeautifulSoup(html_data,'html.parser')


# In[270]:


table = soup.find_all('table', class_ = 'historical_data_table table')
Tab = table[1]


# In[271]:


row = Tab.find_all('tr')
row


# In[277]:


tesla_data = []

for i in row[1:]:
    data = i.text
    tesla_data.append(data.replace('\n',""))


# In[278]:


Year = []
Revenue = []

for i in tesla_data:
    Year.append(i[:10])
    Revenue.append(i[10:])

dict = {'Date': Year,'Revenue (Millions of US $)':Revenue}

tesla_revenue = pd.DataFrame(dict)

tesla_revenue.tail()


# In[243]:


ticker_symbol = "GME"

GameStop_data = yf.Ticker(ticker_symbol)

gme_data = pd.DataFrame(GameStop_data.history(period="max"))
gme_data.reset_index(inplace=True)


# In[244]:


gme_data.head()


# In[ ]:





# In[103]:


url_GME = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

html_data_GME = requests.get(url_GME).text

soup_GME = BeautifulSoup(html_data_GME,'lxml')


# In[217]:


table_GME = soup_GME('table', class_ = 'historical_data_table table')
print(table_GME)


# In[238]:


GME_Data = table_GME[1]


# In[235]:


use_data = []
for i in GME_Data.find_all('tr')[1:]:
    data = i.text
    use_data.append(data.replace('\n',""))


# In[242]:


date = []
revenue = []

for i in use_data:
    date.append(i[:10])
    revenue.append(i[10:])
dict = {'Year':date,'Revenue (Millions of US $)':revenue}

gme_revenue = pd.DataFrame(dict)
gme_revenue.tail()


# In[ ]:


tesla_stock_data


# In[ ]:


tesla_df


# In[251]:


plt.figure(figsize=(16, 8), dpi=150)


# In[ ]:




