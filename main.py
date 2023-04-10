import streamlit as st
import pandas
st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/oczy_piekom.jpg')

with col2:
    st.title("Oksen Śpiwak")
    content = '''Filantrop, kulturysta, entuzjasta ciepłego ciasta
    oraz kandydat na kandytata.(Jakaś suka potraktowała mnie gazem pieprzowym)'''
    st.info(content)

st.write("Co tam słychać? Stare kurwy nie chcą zdychac")

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[10:].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[:10].iterrows():
        st.header(row['title'])