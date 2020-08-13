import streamlit as st 



st.title('Hello World')
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('http://google.com/') ;\
print('Headless Firefox Initialized')
driver.quit()
st.success('selenium works')
try: 
    import nltk
    st.success('nltk works')
except:
    st.text('nltk fails')
import pickle
import os
if not(os.path.exists('data/traingDats.p')):
    os.system('mv traingDats.p?dl=0 data/traingDats.p')
    os.system('mv benchmarks.p?dl=0 data/benchmarks.p')


if os.path.exists("data/traingDats.p?dl=0") and not os.path.exists("data/traingDats.p"):
    os.system('mv traingDats.p?dl=0 data/traingDats.p')
    os.system('mv benchmarks.p?dl=0 data/benchmarks.p')

try:
    pickle.load(open('data/benchmarks.p','rb'))
    st.success('pickle data sources downloaded')
except:
    st.text('fail')

import nltk
try:
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
except:
    nltk.download('punkt')
    nltk.download('stopwords')  
st.success('NLTK data sources downloaded')
  
    #Raise(Exception())