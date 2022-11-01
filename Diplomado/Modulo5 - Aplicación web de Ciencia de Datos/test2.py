import streamlit as st 

sidebar = st.sidebar 
sidebar.title("Esta es la barra lateral.") 
sidebar.write("Aquí van los elementos de entrada.")

# Crear el título para la aplicación web 
st.title("Mi Primera App con Streamlit...") 
st.header("Información sobre el Conjunto de Datos")
st.header("Descripción de los datos ") 
st.write(""" 
import streamlit as st 
st.title("Mi Primera App con Streamlit") 
  
Este es un simple ejemplo de una app para predecir 
  
¡Esta app predice mis datos! 
""") 


#Radio Button
#selected_class = st.radio("Select Class", titanic_data['class'].unique())
#st.write("Selected Class:", selected_class)

#SelectBox
#selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())
#st.write(f"Selected Option: {selected_sex!r}")

"""
	Nota: En la instrucción st.write hay que notar que para el titulo se antepone la letra “f” 
	que indica que se capturara información y en la sección donde se indica la variable al final 
	se pone el signo de admiración y la letra “r” esto indica que se escribirá la opción que se haya elegido.
"""

#Sliders
#optionals = st.beta_expander("Optional Configurations", True) # Se activa el expansor 
#fare_select = optionals.slider(
#    "Select the Fare",
#    min_value=float(titanic_data['fare'].min()),
#    max_value=float(titanic_data['fare'].max())
#)
#subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]  #Contendra el conjunto de datos min y max
#st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}") #Observe que se debe de anteponer la letra “f” al titulo que aparecerá debajo de la barra deslizante.

