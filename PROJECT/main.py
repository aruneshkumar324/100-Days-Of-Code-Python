import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap

df = pd.read_csv("dataset.csv")
m = folium.Map(tiles = 'Stamen Terrain',min_zoom = 1.5)
display(m)