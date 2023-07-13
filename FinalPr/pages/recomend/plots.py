import matplotlib.pyplot as plt
import seaborn as sns
import squarify
from PIL import Image
from wordcloud import WordCloud
import plotly.express as px
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Función para obtener los 25 estilos de cerveza más comunes en el conjunto de datos
def get_top_25_beer_styles(df_Beer):
    # Contar cuántas veces aparece cada tipo de cerveza y devolver los 25 primeros
    return df_Beer['beer/style'].value_counts().head(25).index

# Función para crear un gráfico de barras con los 25 tipos de cerveza más comunes
def plot_most_common_beer_bar(df_Beer):
    # Contar cuántas veces aparece cada tipo de cerveza y seleccionar los 25 primeros
    beer_counts = df_Beer['beer/style'].value_counts().nlargest(25)
    # Crear un nuevo gráfico de tamaño 10x10
    fig, ax = plt.subplots(figsize=(10, 10))
    # Crear un gráfico de barras horizontales
    sns.barplot(x=beer_counts.values, y=beer_counts.index, ax=ax)
    # Título del gráfico
    ax.set_title('Distribución de las 25 cervezas más comunes por tipo')
    # Etiqueta del eje x
    ax.set_xlabel('Cantidad')
    # Etiqueta del eje y
    ax.set_ylabel('Tipo de cerveza')
    # Asegurarse de que el gráfico se ajuste bien a la figura
    fig.tight_layout()
    # Mostrar el gráfico
    st.pyplot(fig)

# Función para crear un gráfico de treemap con los 25 tipos de cerveza más comunes
def plot_most_common_beer_treemap(df_Beer):
    # Contar cuántas veces aparece cada tipo de cerveza y seleccionar los 25 primeros
    beer_counts = df_Beer['beer/style'].value_counts().nlargest(25)
    # Crear una nueva figura de tamaño 12x8
    fig, ax = plt.subplots(figsize=(12, 8))
    # Crear un gráfico de treemap
    squarify.plot(sizes=beer_counts.values, label=beer_counts.index, alpha=0.8, ax=ax)
    # Quitar los ejes
    ax.axis('off')
    # Título del gráfico
    ax.set_title('Distribución de las 25 cervezas más comunes por tipo (Treemap)')
    # Asegurarse de que el gráfico se ajuste bien a la figura
    fig.tight_layout()
    # Mostrar el gráfico
    st.pyplot(fig)

# Función para crear una nube de palabras con los nombres de las cervezas
def plot_beer_wordcloud(df_Beer, img_path):
    # Contar cuántas veces aparece cada nombre de cerveza
    beer_counts = df_Beer['beer/name'].value_counts()
    # Cargar una máscara con la forma de una cerveza
    beer_mask = np.array(Image.open('beer.png'))
    # Crear una nube de palabras con la máscara de la cerveza y otras configuraciones
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100, mask=beer_mask, contour_width=3, contour_color='black')
    # Generar la nube de palabras a partir de las frecuencias de los nombres de las cervezas
    wordcloud.generate_from_frequencies(beer_counts)
    # Crear una nueva figura de tamaño 10x10
    fig, ax = plt.subplots(figsize=(10, 10))
    # Mostrar la nube de palabras
    ax.imshow(wordcloud, interpolation='bilinear')
    # Quitar los ejes
    ax.axis('off')
    # Asegurarse de que el gráfico se ajuste bien a la figura
    fig.tight_layout()
    # Mostrar el gráfico
    st.pyplot(fig)

# Función para crear un histograma con la distribución de los sentimientos
def plot_sentiment_distribution(df_Beer):
    # Crear una nueva figura de tamaño 10x6
    fig, ax = plt.subplots(figsize=(10, 6))
    # Crear un histograma de los sentimientos, ignorando los valores NaN y sin trazar la curva de densidad de kernel
    sns.histplot(df_Beer['sentiment'].dropna(), kde=False, bins=30, ax=ax)
    # Título del gráfico
    ax.set_title('Distribución de los sentimientos')
    # Etiqueta del eje x
    ax.set_xlabel('Sentimiento')
    # Etiqueta del eje y
    ax.set_ylabel('Frecuencia')
    # Mostrar el gráfico
    st.pyplot(fig)

# Función para crear un heatmap con la correlación entre las características de las reseñas
def plot_review_features_correlation(df_Beer):
    # Definir las características de la reseña que se van a correlacionar
    review_features = ['review/appearance', 'review/aroma', 'review/palate', 'review/taste']
    # Calcular la correlación entre estas características
    corr = df_Beer[review_features].corr()
    # Crear una nueva figura de tamaño 10x6
    fig, ax = plt.subplots(figsize=(10, 6))
    # Crear un heatmap de las correlaciones
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    # Título del gráfico
    ax.set_title('Correlación entre las características de las reseñas')
    # Mostrar el gráfico
    st.pyplot(fig)

# Función para crear un gráfico de barras con las 10 cervezas más revisadas
def plot_most_reviewed_beers(df_Beer):
    # Contar cuántas veces aparece cada nombre de cerveza y seleccionar los 10 primeros
    top_beers = df_Beer['beer/name'].value_counts().head(10)
    # Crear una nueva figura de tamaño 10x6
    fig, ax = plt.subplots(figsize=(10, 6))
    # Crear un gráfico de barras con los nombres de las cervezas y el número de reseñas
    sns.barplot(x=top_beers.index, y=top_beers.values, ax=ax)
    # Título del gráfico
    ax.set_title('Las 10 cervezas más revisadas')
    # Etiqueta del eje x
    ax.set_xlabel('Nombre de la cerveza')
    # Etiqueta del eje y
    ax.set_ylabel('Número de reseñas')
    # Rotar las etiquetas del eje x 90 grados para que se puedan leer bien
    plt.xticks(rotation=90)
    # Mostrar el gráfico
    st.pyplot(fig)

# Función para crear un gráfico de burbujas con el sentimiento por estilo de cerveza
def plot_sentiment_beer_style_bubble(df_Beer):
    # Contar cuántas veces aparece cada combinación de estilo de cerveza y etiqueta de sentimiento
    sentiment_counts = df_Beer.groupby(['beer/style', 'sentiment_label']).size().reset_index(name='counts')
    # Crear una nueva columna 'review_count' que contenga la suma total de reseñas para cada combinación de estilo de cerveza y etiqueta de sentimiento
    sentiment_counts['review_count'] = sentiment_counts.groupby(['beer/style', 'sentiment_label'])['counts'].transform('sum')
    # Obtener los 25 estilos de cerveza más comunes
    top_25_beer_styles = get_top_25_beer_styles(df_Beer)
    # Filtrar el dataframe para incluir solo los 25 estilos de cerveza más comunes
    sentiment_counts_top_25 = sentiment_counts[sentiment_counts['beer/style'].isin(top_25_beer_styles)]
    # Crear un gráfico de burbujas con los estilos de cerveza en el eje x, las etiquetas de sentimiento en el eje y, el tamaño de las burbujas correspondiente al número de reseñas y el color de las burbujas correspondiente a la etiqueta de sentimiento
    fig = px.scatter(sentiment_counts_top_25, x='beer/style', y='sentiment_label', size='review_count', color='sentiment_label', hover_name='beer/style', title='Sentiment by Beer Style for Top 25 Beer Styles')
    # Actualizar las etiquetas de los ejes y el ángulo de las etiquetas del eje x
    fig.update_layout(xaxis_tickangle=-45, xaxis_title='Beer Style', yaxis_title='Sentiment')
    # Mostrar el gráfico
    st.plotly_chart(fig)

# Función para crear un boxplot con la distribución de ABV (alcohol por volumen) por estilo de cerveza
def plot_abv_beer_style_box(df_Beer):
    # Filtrar el dataframe para incluir solo los 25 estilos de cerveza más comunes
    top_25_beer_styles = df_Beer[df_Beer['beer/style'].isin(get_top_25_beer_styles(df_Beer))]
    # Crear una nueva figura de tamaño 15x10
    fig, ax = plt.subplots(figsize=(15, 10))
    # Crear un boxplot con los estilos de cerveza en el eje x y el ABV en el eje y
    sns.boxplot(x='beer/style', y='beer/ABV', data=top_25_beer_styles, ax=ax)
    # Rotar las etiquetas del eje x 90 grados para que se puedan leer bien
    plt.xticks(rotation=90)
    # Título del gráfico
    ax.set_title('Distribución de ABV por estilo de cerveza')
    # Etiqueta del eje x
    ax.set_xlabel('Estilo de cerveza')
    # Etiqueta del eje y
    ax.set_ylabel('ABV')
    # Mostrar el gráfico
    st.pyplot(fig)

def plot_3d_scatter_overall_palate_taste(df_Beer):
    # Gráfico de dispersión 3D de calificación general, paladar y sabor para los 10 estilos de cerveza más comunes
    top_10_beer_styles = df_Beer['beer/style'].value_counts().index[:10]
    df_top_10 = df_Beer[df_Beer['beer/style'].isin(top_10_beer_styles)]
    fig = px.scatter_3d(df_top_10, x='review/overall', y='review/palate', z='review/taste', color='beer/style')
    fig.update_layout(title='Relación entre Calificación General, Paladar y Sabor')
    # Mostrar el gráfico
    st.plotly_chart(fig)
