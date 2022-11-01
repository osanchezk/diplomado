#Graficas
#Admite varias bibliotecas de gráficos diferentes,  como Altair, Bokeh, Matplotlib e incluso Plotly
#Admite Vega Lite (gráficos en 2D) y deck.gl (mapas y gráficos en 3D)
#st.line_chart
#st.area_chart
#st.markdown -> Divide información
#fig, ax -> EL primero lo contiene y el segundo lo escribe

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)
st.header("Data Description - Header")

#Histograma
#fig, ax = plt.subplots()  
#ax.hist(titanic_data.fare)
#st.header("Histograma del Titanic")
#st.pyplot(fig) #Ayuda a graficar
#st.markdown("___") #Linea de división

#Grafico de barras
# fig que contendrá la gráfica de barras
# ax que nos servirá para construirlo.
#fig2, ax2 = plt.subplots()
#y_pos = titanic_data['class']
#x_pos = titanic_data['fare']

#ax2.barh(y_pos, x_pos)   # Barra Horizontal
#ax2.set_ylabel("Class")  
#ax2.set_xlabel("Fare")  
#ax2.set_title('¿Cuanto pagaron las clases del Titanic')   
#st.header("Grafica de Barras del Titanic")  

#st.pyplot(fig2)  

#st.markdown("___")

#Grafica de dispersión
fig3, ax3 = plt.subplots()  

ax3.scatter(titanic_data.age, titanic_data.fare)  
ax3.set_xlabel("Edad")  
ax3.set_ylabel("Tarifa")  

st.header("Grafica de Dispersión del Titanic")  

st.pyplot(fig3)   