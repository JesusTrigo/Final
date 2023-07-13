import streamlit as st
import home
from pages.detection import detection
from pages.recomend import recomend
from pages.recomend import plots
#from pages.scrap import home
import pandas as pd
#from pages.recomend.plots import (
    #get_top_25_beer_styles,
    #plot_most_common_beer_bar,
    #plot_most_common_beer_treemap,
    #plot_beer_wordcloud,
    #plot_sentiment_distribution,
    #plot_review_features_correlation,
    #plot_most_reviewed_beers,
    #plot_sentiment_beer_style_bubble,
    #plot_abv_beer_style_box,
    #plot_3d_scatter_overall_palate_taste
#)

#st.set_option('deprecation.showPyplotGlobalUse', False)

#@st.cache_data
#def read_csv_streamlit():
   # url = "https://drive.google.com/u/0/uc?id=1ePhuTPZWNkW4Nw634dXxV21fneJRgNWo&export=download&confirm=t&uuid=61491d58-19cc-11ee-be56-0242ac120002"
    #df = pd.read_csv(url)
    #return df
    
#df_Beer = read_csv_streamlit()  
#def main():
    # Configurar la barra lateral para seleccionar la página
    #st.sidebar.title('Selector de Páginas')
    #page = st.sidebar.selectbox('Seleccione una página', options=['Home', 'Detección', 'Recomendación', 'Scraping'])

    # Dependiendo de la página seleccionada, mostrar el contenido correspondiente
    #if page == 'Home':
     #   home.main()
    #elif page == 'Detección':
     #   detection.main()
    #elif page == 'Recomendación':
    #    recomend.main() # Esta función ahora manejará tanto recomend como plots
   #elif page == 'Scraping':
   #     home.main()

#if __name__ == "__main__":
 #  main()


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
        recomend_option = st.sidebar.selectbox('Seleccione una opción', options=['Código', 'Gráficos']) # Nuevo selectbox para sub-selección
        if recomend_option == 'Código':
            recomend.main()
        elif recomend_option == 'Gráficos':
            plots.get_top_25_beer_styles(plots.df_Beer)
            plots.plot_most_common_beer_bar(plots.df_Beer)
            plots.plot_most_common_beer_treemap(plots.df_Beer)
            plots.plot_beer_wordcloud(plots.df_Beer)
            plots.plot_sentiment_distribution(plots.df_Beer)
            plots.plot_review_features_correlation(plots.df_Beer)
            plots.plot_most_reviewed_beers(plots.df_Beer)
            plots.plot_sentiment_beer_style_bubble(plots.df_Beer)
            plots.plot_abv_beer_style_box(df_Beer)
            plots.plot_3d_scatter_overall_palate_taste(plots.df_Beer)
    elif page == 'Scraping':
        home.main()

if __name__ == "__main__":
    main()
