import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Leo_Livs.')

st.info('DJ, General Contractor, Real Estate Investor, Python Developer')

icon_size = 20

# st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/Leo_livs/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/leonel-lopez-9b64a2172', 'Follow me on LinkedIn', icon_size)
# st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
