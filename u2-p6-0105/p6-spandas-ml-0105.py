
import pandas as pd
import numpy as np

series_amigos=["pedro","hugo","Farfan","jesse","morgan","Iker","yukimiya"]
print("-------Serie listado de amigos NC 0105")
amigos=pd.Series(series_amigos)
print(amigos)

series_billetes=[20,50,100,200,500,1000]
print("-------Serie listado de billetes NC 0105")
billetes=pd.Series(series_billetes)
print(billetes)

series_billetes=[20,50,100,200,500,1000]
serie_letras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("-------Serie listado nombre y valor de billetes MX NC 0105 NC 0105")
billetes=pd.Series(series_billetes,serie_letras)
print(billetes)

# diccionario dataframe
# diccionario de valor monedas y nombre
print("datos de diccionario a dataframe en pandas ")
dic_monedas={
    "series_billetes":[20,50,100,200,500,1000],
    "serie_letras":["veinte","cincuenta","cien","docientos","quinientos","mil"]
}

serie_letras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("-------Serie listado nombre y valor de billetes MX NC 0105 NC 0105")
billetes=pd.Series(dic_monedas,index=["A","B","C","D","E","F"])
print(billetes)
print("casa de csmbio de Iker Montoya NC 0105")


