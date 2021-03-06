# -*- coding: utf-8 -*-
"""AkiraChix Rates.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jjf6hfCNIEdHEbTR53nOt7FDgoL_xjSW
"""

import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

!pip install geopandas

import geopandas as gpd

df=pd.read_csv('/content/Akirachix Intakes - Sheet1 (1).csv')
df.head()

df.info()

df.describe

df1 = df.sort_values(by = ['Total Number of intakes'],ascending = False).reset_index()

Rates= px.bar(df1, x = 'Country', y = 'Total Number of intakes', color = 'Total Number of intakes',
             color_continuous_scale = 'reds')

Rates.update_layout(title = 'Total number of intakes from 2010-2021',
                  title_x = 0.5,
                  title_font = dict(size = 18, color = 'Green'))
Rates.show()

df1 = df.sort_values(by = ['Average Income Rates($)'],ascending = False).reset_index()

Rates= px.bar(df1, x = 'Country', y = 'Average Income Rates($)', color = 'Average Income Rates($)',
             color_continuous_scale = 'oranges')

Rates.update_layout(title = 'Average Income Rates($) from 2010-2021',
                  title_x = 0.5,
                  title_font = dict(size = 18, color = 'Green'))
Rates.show()

df1 = df.sort_values(by = ['Total number of Graduates'],ascending = False).reset_index()

Rates= px.bar(df1, x = 'Country', y = 'Total number of Graduates', color = 'Total number of Graduates',
             color_continuous_scale = 'oranges')

Rates.update_layout(title = 'Total number of Graduates from 2010-2021',
                  title_x = 0.5,
                  title_font = dict(size = 18, color = 'Green'))
Rates.show()

df1 = df.sort_values(by=['Total Number of intakes'],ascending = False).reset_index()

fig = px.choropleth(df1,
                    locations = 'Country',
                    locationmode = 'country names',
                    color = 'Total Number of intakes',
                    scope = 'africa',
                    hover_name = 'Country',
                    color_continuous_scale = 'reds')

fig.update_layout(title= 'Total Number of intakes among the East African Countries',
                  title_x = 0.5,
                  title_font = dict(size = 16, color = 'Darkblue'),
                  geo = dict(showframe = False,
                             showcoastlines = False,
                             projection_type = 'equirectangular'))
fig.show()

# # getting inbuilt dataset from geopandas
# world_data=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# # plot the world map
# axis=world_data[world_data.continent==" Africa"].plot(color="purple",edgecolor="black")

# df.plot(ax=axis,color="black")
# plt.title("East African Countries")

# fig=matplotlib.pyplot.gcf()
# fig.set_size_inches(9.6)
# fig.savefig("Matplot.png",dpi=200)
# plt.show()