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
    #Raise(Exception())