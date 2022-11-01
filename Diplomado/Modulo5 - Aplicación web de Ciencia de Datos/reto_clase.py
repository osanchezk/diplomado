
import streamlit as st 
import pandas as pd
import codecs

sidebar = st.sidebar
sidebar.title("Filtro - Netflix") 

st.title("Catalogo Netflix")

@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

videos = load_data(100)

agree = sidebar.checkbox('Filmes recuperados')

if agree:
	st.write('Great!')
	st.write(videos)
	st.markdown("___")

selected_sex = sidebar.selectbox("Select Movie", videos['name'].unique())

@st.cache
def load_data_byD(dat):
  filtered_data_byDir = videos[videos["name"] == dat]
  return filtered_data_byDir

if selected_sex:
	filterbydir = load_data_byD(selected_sex)
	count_row = filterbydir.shape[0]
	st.write(f"Total Items: {count_row}")
	st.dataframe(filterbydir["director"])
	st.markdown("___")

def load_data_bytitle(title):
	filtered_data_bytit = videos[videos['name'].str.upper().str.contains(title)]
	return filtered_data_bytit

tit = sidebar.text_input("By title: ")

if (tit):
  filterbytitle = load_data_bytitle(tit.upper())
  count_row = filterbytitle.shape[0]
  st.title('Coincidencias')
  st.write(f"Total Titles: {count_row}")
  st.dataframe(filterbytitle)