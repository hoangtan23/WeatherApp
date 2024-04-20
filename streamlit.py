
import streamlit as st
import pandas as pd


from datetime import datetime
from pytz import timezone


def get_data():
    path = r'C:\Users\Admin\Documents\WeatherApp\edit.csv'
    return pd.read_csv(path)
df = get_data()



st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard Weather')

city = list(df["City"].unique())[::-1]
st.sidebar.subheader('Filter City')
city_filter = st.sidebar.selectbox('Select City', city)
df_select_city = df[df['City'] == city_filter]

st.sidebar.subheader('Line chart parameters')
plot_data_line = st.sidebar.multiselect('Select data', ['Temperature_max', 'Temperature_min','Uv_max'], ['Temperature_max', 'Temperature_min','Uv_max'])

st.sidebar.subheader('Scatter chart parameters')
plot_data_scatter = st.sidebar.multiselect('Select data', ['Amount_rain', 'Precipitation_rain','Wind_max'], ['Amount_rain', 'Precipitation_rain','Wind_max'])

st.sidebar.markdown('''
---
Created with ❤️ by Tran Hoang Tan.
''')

# Row A
temp_curr = str(df_select_city['Temp_curr2'].head(1).values) + '°C'

temp_curr_replace = temp_curr.translate( { ord(i): None for i in '[]'} )

date = str(datetime.strftime(datetime.now(timezone('Asia/Bangkok')),"%Y-%m-%d - %H:%M:%S"))

col1, col2 = st.columns((2,8))
with col1:
    st.markdown('### Temperature Current')
    col1.metric(date,temp_curr_replace,'-3°C')

with col2:
    st.markdown('### Line chart')
    st.line_chart(df_select_city, x = 'Date', y = plot_data_line)

st.markdown('### Scatter  chart')
st.scatter_chart(df_select_city,x='Date',y=plot_data_scatter)

