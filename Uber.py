import streamlit as st
import pandas as pd
import numpy as np


st.title("Uber Pickups in New York")

DATE_COLUMN = ('date/time'
DATE_URL = ('HTTPS://S3-US-WEST-2.AMAZONAWS.COM/)'
        'streamlit-demo-data/uber-raw-data-sep14.csv.gz')