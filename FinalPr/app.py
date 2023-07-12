import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
from PIL import Image
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
import pandas as pdimport streamlit as st
import pandas as pd
import plots
import home
from pages.detection import detection
from pages.recomend import recomend
from pages.scrap import scrap

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
