import streamlit as st
import home
from pages.detection import detection
from pages.recomend import recomend
from pages.recomend.plots import plots
#from pages.scrap import home


def main():
    # Configurar la barra lateral para seleccionar la página
    st.sidebar.title('Selector de Páginas')
    page = st.sidebar.selectbox('Seleccione una página', options=['Home', 'Detección', 'Recomendación', 'Scraping'])

    # Dependiendo de la página seleccionada, mostrar el contenido correspondiente
    if page == 'Home':
        home.main()
    elif page == 'Detección':
        detection.main()
    elif page == 'Recomendación':
        recomend.main()
    elif page == 'Plots':
        plots.main()
    elif page == 'Scraping':
        home.main()

if __name__ == "__main__":
    main()
