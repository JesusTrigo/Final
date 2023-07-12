pip install -r requirements.txt
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

PAGES = {
    "Home": home,
    "Detection Page": detection,
    "Recommendation Page": recomend,
    "Scrap Page": scrap
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]

    # Cada página tiene una función run()
    page.run('home')
    page.run('detection')
    page.run('recomend')
    page.run('scrap')

if __name__ == "__main__":
    main()
