import streamlit as st
import home
from pages.detection import detection
from pages.recomend import recomend, plots
from pages.scrap import scrap

df_Beer = recomend.df_Beer

def main():
    # Configurando la barra lateral para seleccionar la página
    st.sidebar.title('Selector de Páginas')
    page = st.sidebar.selectbox('Seleccione una página', options=['Home', 'Detección', 'Recomendación', 'Scraping'])

    # Dependiendo de la página seleccionada, mostrar el contenido correspondiente
    if page == 'Home':
        home.main()
    elif page == 'Detección':
        detection.main()
    elif page == 'Recomendación':
        st.sidebar.title('Selector de Recomendación') # Nuevo título para la sub-selección
        recomend_option = st.sidebar.selectbox('Seleccione una opción', options=['App', 'Gráficos']) # Nuevo selectbox para sub-selección
        if recomend_option == 'App':
            recomend.main()
        elif recomend_option == 'Gráficos':
            plots.intro()
            plots.get_top_25_beer_styles(df_Beer)
            plots.plot_most_common_beer_bar(df_Beer)
            plots.plot_beer_wordcloud(df_Beer)
            plots.plot_most_common_beer_treemap(df_Beer)
            plots.plot_sentiment_distribution(df_Beer)
            plots.plot_review_features_correlation(df_Beer)
            plots.plot_most_reviewed_beers(df_Beer)
            plots.plot_sentiment_beer_style_bubble(df_Beer)
            plots.plot_abv_beer_style_box(df_Beer)
            plots.plot_3d_scatter_overall_palate_taste(df_Beer)
    elif page == 'Scraping':
        scrap.main()

if __name__ == "__main__":
    main()
