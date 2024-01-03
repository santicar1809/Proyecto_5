# %% [markdown]
# ## Análisis exploratorio de datos para proyecto 5

# %% [markdown]
# **Primero vamos a importar las librerías**

# %%
import pandas as pd
import plotly.express as px
import streamlit as st


# %%
df=pd.read_csv('vehicles_us.csv')
print(df.head())
print(df.info())

# %% [markdown]
# **Identificamos los valores ausentes y duplicados.**

# %%
print('Ausentes llamadas:\n', df.isna().sum())

# %%
#Contamos los valores que tenemos de cada categoría
for columns in df.columns:
    print(df[columns].value_counts())
    

# %%
#LLenamos los ausentes con la media
df['model_year']=df['model_year'].fillna(df['model_year'].mean())
df['cylinders']=df['cylinders'].fillna(df['cylinders'].mean())
df['odometer']=df['odometer'].fillna(df['odometer'].mean())
df['is_4wd']=df['is_4wd'].fillna(0)


# %%
#Duplicados
print('Duplicados:\n', df.duplicated().sum())

# %% [markdown]
# ## Análisis exploratorio de datos
st.header('Análisis exploratorio de datos')
# %%
build_histogram = st.checkbox('Construir un histograma')
build_scatterplot = st.checkbox('Construir un diagrama de dispersión')
build_barplot = st.checkbox('Construir un diagrama de barras')
# %%
if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma')
    #Histogram
    fig = px.histogram(df, x="price")
    fig.show()
    st.plotly_chart(fig, use_container_width=True)
# %%
if build_scatterplot: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma')
    #Scatter plot
    fig = px.scatter(df, x="model_year", y="price") # crear un gráfico de dispersión
    fig.show() # crear gráfico de dispersión 
    st.plotly_chart(fig, use_container_width=True) 
# %%
if build_barplot: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma')
    #Bar plot
    fig = px.histogram(df, x="paint_color", y='price', title="Color vs Price",histfunc='avg')
    fig.show()
    st.plotly_chart(fig, use_container_width=True)
