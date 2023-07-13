import streamlit as st
import home
from pages.detection import detection
from pages.recomend import recomend, plots
from pages.scrap import scrap

df_Beer = recomend.df_Beer

def main():
    # Configurando la barra lateral para seleccionar la página
    st.sidebar.title('Selector de Páginas')
    if st.sidebar.button('Home'):
        home.main()

    if st.sidebar.button('Detección'):
        detection.main()

    if st.sidebar.button('Recomendación'):
        st.sidebar.title('Selector de Recomendación') # Nuevo título para la sub-selección
        if st.sidebar.button('App'):
            recomend.main()

        if st.sidebar.button('Gráficos'):
            plots.intro()
            plots.get_top_25_beer_styles(df_Beer)
            plots.plot_most_common_beer_bar(df_Beer)
            plots.plot_most_reviewed_beers(df_Beer)
            plots.plot_sentiment_distribution(df_Beer)
            plots.plot_most_common_beer_treemap(df_Beer)
            plots.plot_sentiment_beer_style_bubble(df_Beer)
            plots.plot_review_features_correlation(df_Beer)
            plots.plot_abv_beer_style_box(df_Beer)
            plots.plot_3d_scatter_overall_palate_taste(df_Beer)
            plots.plot_beer_wordcloud(df_Beer)

    if st.sidebar.button('Scraping'):
        scrap.main()

if __name__ == "__main__":
    main()
