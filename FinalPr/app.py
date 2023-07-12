import streamlit as st
from pages.detection.detection import detection
from pages.recomend.recomend import recomend
from pages.scrap.scrap import scrap

# Configurar la barra lateral para seleccionar la página
st.sidebar.title('Selector de Páginas')
page = st.sidebar.selectbox('Seleccione una página', options=['Detección', 'Recomendación', 'Scraping'])

# Dependiendo de la página seleccionada, mostrar el contenido correspondiente
if page == 'Recomendación':
    recomend.main()
elif page == 'Scraping':
    scrap.main()

if __name__ == "__main__":
    main()
