import streamlit as st
import pandas as pd
import numpy as np


st.title("Uber Pickups in New York")

DATE_COLUMN = 'date/time'
DATE_URL = ('HTTPS://S3-US-WEST-2.AMAZONAWS.COM/)'
        'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
        data=pd.read_csv(DATA_UPL, nrows=nrows)
        lowercase=lambda x:str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
        return data

data_load_state=st.text("Loading Data...")
data=load_data(10000)
data_load_state.text("Loading Data Done!")