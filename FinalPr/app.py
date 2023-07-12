import streamlit as st
import home
from pages.detection import detection
from pages.recomend import recomend
import sys
sys.path.append('FinalPr/pages/recomend/plots/plots.py')
from pages.recomend.plots import plots # Importa main de plots.py como plots
#from pages.scrap import home

#def main():
#    # Configurar la barra lateral para seleccionar la página
#    st.sidebar.title('Selector de Páginas')
#    page = st.sidebar.selectbox('Seleccione una página', options=['Home', 'Detección', 'Recomendación', 'Scraping'])

 #   # Dependiendo de la página seleccionada, mostrar el contenido correspondiente
#    if page == 'Home':
#        home.main()
#    elif page == 'Detección':
 #       detection.main()
#   elif page == 'Recomendación':
 #       recomend.main()
  #  elif page == 'Plots':
  #      plots.main()
 #  elif page == 'Scraping':
  #      home.main()

#if __name__ == "__main__":
#    main()


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
            plots() # Llama a plots(), que se refiere a main() en plots.py
    elif page == 'Scraping':
        home.main()

if __name__ == "__main__":
    main()
