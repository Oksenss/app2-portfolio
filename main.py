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

col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+ row['image'])
        st.write(f"[Source code]({row['url']})")