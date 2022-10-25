import pandas as pd
personajesSW = pd.read_csv("characters.csv")
#personajesSW["height_m"] = personajesSW["height"] / 100
#print(personajesSW.head())
personajesSW["imc"] = personajesSW["mass"] / (personajesSW["height"] / 100 ) ** 2

seleccion = personajesSW[['name', 'mass']]
print(personajesSW.head())
print(seleccion)