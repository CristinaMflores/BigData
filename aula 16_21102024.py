import pandas as pd

df_categoria = pd.read_csv('superstore.csv') 
print(df_categoria.head()) # Exibe as cinco primeiras linhas
print(df_categoria.tail()) # Exibe as cinco últimas linhas
print(df_categoria.to_string()) # Exibe o DataFrame completo como uma string, útil para visualização    
           
df_filtrado= df_categoria[df_categoria['City']=='Los Angeles']
print(df_filtrado)
