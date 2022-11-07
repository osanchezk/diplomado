"""
Módulo 5: Aplicación web de Ciencia de Datos
Reto: Análisis de deserción de empleados
Objetivos: 

	• Realizar un análisis de los datos para conocer su estructura y contenido, y así relacionarla
	  con los requisitos del reto
	• Desarrollar funciones que nos permitan obtener datos de una manera eficiente
	• Crear una aplicación web con diversas secciones que nos permitan visualizar datos
	  desde diversos puntos de vista
	• Visualizar información relevante en gráficas para realizar procesos de análisis

Nota: Este programa se realizó de forma directa desde el editor de sublime, se ejecutó con los siguientes comandos desde consola:
	1.- ngrok http 8501
	2.- streamlit run employees.py

Autor: Omar K Sánchez Miranda
Fecha: 07 de Noviembre, 2022

"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

DATA = 'Employees.csv'

#nrow: Default 500
defaultRows = 500;

### Funciones

@st.cache
def load_data(dat, numReg):
	getData = pd.read_csv(dat, nrows=numReg)
	return getData

@st.cache
def findEmployees(name, getColumn):
	showData = load_data(DATA, defaultRows)
	filteredDataByname = showData[showData[getColumn].str.contains(name)]
	return filteredDataByname

@st.cache
def findEmployeesEducLevel(educLevelId):
	showData = load_data(DATA, defaultRows)
	filteredDataByEducLevel = showData[showData['Education_Level'] == educLevelId]
	return filteredDataByEducLevel

@st.cache
def findEmployeesCity(cityId):
	showData = load_data(DATA, defaultRows)
	filteredDataByCity = showData[showData['Hometown'] == cityId]
	return filteredDataByCity

@st.cache
def findEmployeesUnit(unitId):
	showData = load_data(DATA, defaultRows)
	filteredDataByUnit = showData[showData['Unit'] == unitId]
	return filteredDataByUnit

def getCount(dat):
	return dat.shape[0]

####################

st.markdown("<h1 style='text-align: center; font-size:18px; color: #15498f;'>Reto 5: Análisis de deserción de empleados</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Autor: Omar K Sánchez Miranda</h2>", unsafe_allow_html=True)
st.markdown("___")

####################
#Sidebar
####################

sidebar = st.sidebar
sidebar.markdown("<span style='text-align: center; font-weight: 900; font-size:18px; color: #15498f;'>Filtros: </span>", unsafe_allow_html=True) 

#Sidebar -Checkbox
agree = sidebar.checkbox('Employee list')
sidebar.markdown("___")
if agree:
	dataLoadState = st.text("Loading data...")
	showData = load_data(DATA, defaultRows)
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Employee List</h2>", unsafe_allow_html=True)
	st.write(showData)
	st.write("Total Rows: ", getCount(showData))
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar - Text Input
getName = sidebar.text_input("Write your search: ")
choseColumn = sidebar.radio("Choose one: ",('Employee_ID', 'Hometown', 'Unit'))
sidebar.markdown("___")
if getName and choseColumn:
	dataLoadState = st.text("Loading data...")
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Employee Filter by: Employee_ID, Hometown, Unit </h2>", unsafe_allow_html=True)
	getListByName = findEmployees(getName, choseColumn)
	st.write(getListByName)
	st.write("Total Rows: ", getCount(getListByName))
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar - selectedbox -> Education_Level
showData = load_data(DATA, defaultRows)
selectedEducLevel = st.sidebar.selectbox("Choose a Education Level: ", sorted(showData['Education_Level'].unique()))
btnFilterbyEducLevel = st.sidebar.button('Filter', key="1")
sidebar.markdown("___")
if (btnFilterbyEducLevel):
	dataLoadState = st.text("Loading data...")
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Filter By Education Level </h2>", unsafe_allow_html=True)
	filterbyEducLevel = findEmployeesEducLevel(selectedEducLevel)
	st.write(filterbyEducLevel)
	st.write("Total Rows: ", getCount(filterbyEducLevel))
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar - selectedbox -> Hometown
selectedCity = st.sidebar.selectbox("Choose a City: ", sorted(showData['Hometown'].unique()))
btnFilterbyCity = st.sidebar.button('Filter', key="2")
sidebar.markdown("___")
if btnFilterbyCity:
	dataLoadState = st.text("Loading data...")
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Filter By Hometown </h2>", unsafe_allow_html=True)
	filterbyCity = findEmployeesCity(selectedCity)
	st.write(filterbyCity)
	st.write("Total Rows: ", getCount(filterbyCity))
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar - selectedbox -> Unit
selectedUnit = st.sidebar.selectbox("Choose a Unit: ", sorted(showData['Unit'].unique()))
btnFilterbyUnit = st.sidebar.button('Filter', key="3")
sidebar.markdown("___")
if btnFilterbyUnit:
	dataLoadState = st.text("Loading data...")
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Filter By Unit </h2>", unsafe_allow_html=True)
	filterbyUnit = findEmployeesUnit(selectedUnit)
	st.write(filterbyUnit)
	st.write("Total Rows: ", getCount(filterbyUnit))
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar -Histogram - Age
agreeHist = sidebar.checkbox('Show Histogram Graph by Age')
sidebar.markdown("___")
if agreeHist:
	dataLoadState = st.text("Loading data...")
	showData = load_data(DATA, defaultRows)
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Histogram Graph by Age</h2>", unsafe_allow_html=True)
	fig1, ax1 = plt.subplots()  
	ax1.hist(showData['Age'], bins=20)
	st.pyplot(fig1)
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar -Bar - Unit
agreeBar = sidebar.checkbox('Show Bar Graph by Unit')
sidebar.markdown("___")
if agreeBar:
	dataLoadState = st.text("Loading data...")
	showData = load_data(DATA, defaultRows)
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Bar Graph by Unit</h2>", unsafe_allow_html=True)
	countDataUnit = showData[['Employee_ID', 'Unit']].groupby('Unit').count()
	st.bar_chart(countDataUnit)
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar -Bar - Hometown
agreeBar2 = sidebar.checkbox('Show Bar Graph by Hometown')
sidebar.markdown("___")
if agreeBar2:
	dataLoadState = st.text("Loading data...")
	showData = load_data(DATA, defaultRows)
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Bar Graph by Hometown</h2>", unsafe_allow_html=True)
	countDataHometown = showData[['Hometown', 'Employee_ID']].groupby('Hometown').count()
	st.markdown("<span style='font-size:20px; color: #15498f;'>Lebanon</span> tiene el mayor índice de deserción", unsafe_allow_html=True)
	st.bar_chart(countDataHometown)
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar -Line - Age vs Attrition_rate
agreeLine1 = sidebar.checkbox('Show Line Graph: Age vs Attrition_rate')
sidebar.markdown("___")
if agreeLine1:
	dataLoadState = st.text("Loading data...")
	showData = load_data(DATA, defaultRows)
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Line Graph: Age vs Attrition_rate</h2>", unsafe_allow_html=True)
	st.markdown("Por lo que veo en la gráfica puedo interpretar que el índice de deserción es bajo")
	st.line_chart(showData, x="Age", y="Attrition_rate")
	dataLoadState.text("Done!")
	st.markdown("___")

#Sidebar -Line - Time_of_service vs Attrition_rate
agreeLine2 = sidebar.checkbox('Show Line Graph: Time_of_service vs Attrition_rate')
sidebar.markdown("___")
if agreeLine2:
	dataLoadState = st.text("Loading data...")
	showData = load_data(DATA, defaultRows)
	st.markdown("<h2 style='text-align: center; font-size:14px; color: #15498f;'>Line Graph: Time_of_service vs Attrition_rate</h2>", unsafe_allow_html=True)
	st.markdown("Por lo que veo en la gráfica puedo interpretar que el índice de deserción es bajo")
	st.line_chart(showData, x="Time_of_service", y="Attrition_rate")
	dataLoadState.text("Done!")
	st.markdown("___")
