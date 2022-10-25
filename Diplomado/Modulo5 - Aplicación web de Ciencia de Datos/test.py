#GitHub - Personal Token: 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
#ngrok http 8501
#streamlit run test.py

import streamlit as st
import pandas as pd

#Primer Programa
#st.title("Mi primer App")
#st.header("Información sobre el conjunto de Datos")

#Segundo Programa
#names_data = pd.read_csv("dataset.csv")

#st.title('Streamlit and Pandas - Omar')
#st.dataframe(names_data)

#Tercer Programa
#@st.cache
#def load_data(nrows):
#    data = pd.read_csv("dataset.csv", nrows=nrows)
#    return data
#"""
#data_load_state = st.text("Loading data...")
#data = load_data(10)
#data_load_state.text("Done! Using st.cache")
#st.dataframe(data)

#Cuarto Programa
#@st.cache
#def load_data_byname(name):
#  data = pd.read_csv("dataset.csv")
#  filtered_data_byname = data[data['name'].str.contains(name)]
#  return filtered_data_byname


#myname = st.text_input("Name: ")
#if (myname):
#  filterbyname = load_data_byname(myname)
#  count_row = filterbyname.shape[0]
#  st.title('Buscador por nombres - Omar')
#  st.write(f"Total Names: {count_row}")
#  st.dataframe(filterbyname)

#Quinto programa
#st.title("streamlit - Search Range")
#DATA_URL = "dataset.csv"

#@st.cache
#def load_data_byrange(startid, endid):
#  data = pd.read_csv(DATA_URL)
#  filtered_data_byrange = data[(data["index"]>=startid) & (data["index"]<=endid)]
#  return filtered_data_byrange

#startid = st.text_input("Start Index:")
#endid = st.text_input("End Date:")
#btnRange = st.button("Search by range")

#if (btnRange):
#  filterbyrange = load_data_byrange(int(startid), int(endid))
#  count_row = filterbyrange.shape[0]
#  st.write(f"Total items: {count_row}")

#  st.dataframe(filterbyrange)

#Sexto Programa
st.title("streamlit - Filter by sex")
DATA_URL = "dataset.csv"
data = pd.read_csv(DATA_URL)

@st.cache
def load_data():
  data = pd.read_csv(DATA_URL)
  return data

@st.cache
def load_data_bysex(sex):
  data=pd.read_csv(DATA_URL)
  filtered_data_bysex = data[data["sex"] == sex]
  return filtered_data_bysex

data = load_data()

selected_sex = st.selectbox("Select sex", data['sex'].unique())
btnFilterbySex = st.button("Filter by sex")

if (btnFilterbySex):
  filterbysex = load_data_bysex (selected_sex)
  count_row = filterbysex.shape[0]
  st.write(f"Total Items: {count_row}")

  st.dataframe(filterbysex)

