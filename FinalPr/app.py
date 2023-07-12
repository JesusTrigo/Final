import streamlit as st
from pages.detection.detection import app as detection
from pages.recomend.recomend import app as recomend
from pages.scrap.scrap import app as scrap

# Configurar la barra lateral para seleccionar la página
st.sidebar.title('Selector de Páginas')
page = st.sidebar.selectbox('Seleccione una página', options=['Detección', 'Recomendación', 'Scraping'])

# Dependiendo de la página seleccionada, mostrar el contenido correspondiente
if page == 'Detección':
    detection.main()
elif page == 'Recomendación':
    recomend.main()
elif page == 'Scraping':
    scrap.main()

if __name__ == "__main__":
    main()
