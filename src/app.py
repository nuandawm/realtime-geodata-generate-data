import pandas as pd
import contextily as cx
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import osmnx

from keplergl import KeplerGl
from shapely.geometry import shape

if __name__ == "__main__":
    df_commuter = pd.read_csv("./data/data.csv")

    osmnx.config(use_cache=True, log_console=True) 

    query_city = {'city': 'City of London'}

    gdf = osmnx.geocode_to_gdf(query_city)

    print(gdf.head())
