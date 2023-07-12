import streamlit as st
import pandas as pd
import numpy as np
#import subprocess
from . import plots

st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def read_csv_streamlit():
    url = "https://drive.google.com/u/0/uc?id=1ePhuTPZWNkW4Nw634dXxV21fneJRgNWo&export=download&confirm=t&uuid=61491d58-19cc-11ee-be56-0242ac120002"
    df = pd.read_csv(url)
    return df

def main():
    url = "https://drive.google.com/u/0/uc?id=1ePhuTPZWNkW4Nw634dXxV21fneJRgNWo&export=download&confirm=t&uuid=61491d58-19cc-11ee-be56-0242ac120002"
    df_Beer = read_csv_streamlit()
    df_display = df_Beer.head()

    st.subheader("Vista previa del DataFrame:")
    st.write(df_display)

    matriz_df = df_Beer.pivot_table(
        values='review/overall',
        index='review/profileName',
        columns='beer/style',
        aggfunc='max'
    )

    all_beers = matriz_df.columns.tolist()

    st.title("¡Hola! Vamos a recomendarte una cerveza según tus gustos previos...")
    st.write(' ')
    st.subheader("El proceso demora unos segundos debido a la cantidad de datos, gracias por su paciencia")
    st.write(' ')

    with st.form(key='my_form'):
        beer_choice1 = st.selectbox('Selecciona tu primer estilo de cerveza:', all_beers, key="beer1")
        rating1 = st.slider('Califica el primer estilo de cerveza:', 0.0, 5.0, step=0.5, key="rating1")

        beer_choice2 = st.selectbox('Selecciona tu segundo estilo de cerveza:', [beer for beer in all_beers if beer != beer_choice1], key="beer2")
        rating2 = st.slider('Califica el segundo estilo de cerveza:', 0.0, 5.0, step=0.5, key="rating2")

        beer_choice3 = st.selectbox('Selecciona tu tercer estilo de cerveza:', [beer for beer in all_beers if beer != beer_choice1 and beer != beer_choice2], key="beer3")
        rating3 = st.slider('Califica el tercer estilo de cerveza:', 0.0, 5.0, step=0.5, key="rating3")

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.session_state.new_user_ratings = {
            beer_choice1: rating1,
            beer_choice2: rating2,
            beer_choice3: rating3
        }

        st.subheader("Los estilos seleccionados y sus calificaciones son:")
        st.write(st.session_state.new_user_ratings)

        nuevo_usuario_serie = pd.Series(st.session_state.new_user_ratings, name='Nuevo Usuario')
        matriz_df.loc['Nuevo Usuario'] = nuevo_usuario_serie

        cervezas_calificadas = list(st.session_state.new_user_ratings.keys())
        usuarios_similares = matriz_df.dropna(subset=cervezas_calificadas)
        usuarios_similares = usuarios_similares.apply(pd.to_numeric, errors='coerce')

        nuevo_usuario_ratings = usuarios_similares.loc['Nuevo Usuario']
        correlaciones = usuarios_similares.apply(lambda row: row.corr(nuevo_usuario_ratings), axis=1)

        correlaciones_df = pd.DataFrame(correlaciones, columns=['correlation'])
        usuarios_similares['corr'] = correlaciones_df['correlation']

        rating_matrix_subset = usuarios_similares.drop("Nuevo Usuario").drop(usuarios_similares.dropna(axis=1).columns, axis=1)
        correlaciones_ajustadas = correlaciones_df.loc[rating_matrix_subset.index].values.reshape(-1, 1)

        weighted_rating_matrix = rating_matrix_subset.values * correlaciones_ajustadas
        weighted_rating_matrix_sum = np.nansum(weighted_rating_matrix, axis=0)
        similarity_sum = np.nansum(np.abs(correlaciones_df), axis=0)

        predicted_ratings = weighted_rating_matrix_sum / similarity_sum

        recommended_beer_indices = np.argsort(-predicted_ratings)[:5]
        recommended_beers = matriz_df.columns[recommended_beer_indices]

        recommended_style = recommended_beers[0]

        beers_of_recommended_style = df_Beer[df_Beer['beer/style'] == recommended_style]
        highest_rated_beer = beers_of_recommended_style.loc[beers_of_recommended_style['review/overall'].idxmax()]['beer/name']

        st.markdown(
            f'Según tus preferencias, la recomendación por _Estilo de Cerveza_ que debes probar es:<br><b>{recommended_style}</b>, '
            f'<br><br>La _Cerveza_ recomendada es:<br><b>{highest_rated_beer}</b>.',
            unsafe_allow_html=True
        )
        
    plots.plot_most_common_beer_bar(df_Beer)
    plots.plot_most_common_beer_treemap(df_Beer)
    plots.plot_beer_wordcloud(df_Beer)
    plots.plot_sentiment_distribution(df_Beer)
    plots.plot_review_features_correlation(df_Beer)
    plots.plot_most_reviewed_beers(df_Beer)
    plots.plot_sentiment_beer_style_bubble(df_Beer)
    plots.plot_abv_beer_style_box(df_Beer)
    #plots.plot_3d_scatter_overall_palate_taste(df_Beer)

if __name__ == "__main__":
    main()











