# %%
#import dependencies 
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pdblp as bbg
from datetime import date
from xbbg import blp

ticker = st.text_input('Ticker', 'HD US Equity')

con = bbg.BCon(port=8194, timeout=50000, debug=False)
con.debug = False
con.start()
today_date = date.today()
today = today_date.strftime("%Y%m%d")

last_price_s = con.bdh(ticker, "PX_LAST", start_date='20000101',end_date=today)
last_price_s.index = last_price_s.index.rename('Date')
last_price_s.columns = [ticker]

last_price_fig = px.line(last_price_s, title='<b>US Consumer Price Index (CPI)<b>')
st.plotly_chart(last_price_fig)
        