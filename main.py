import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/oczy_piekom.jpg')

with col2:
    st.title("Oksen Śpiwak")
    content = '''Filantrop, kulturysta, entuzjasta ciepłego ciasta
    oraz kandydat na kandytata.(Jakaś suka potraktowała mnie gazem pieprzowym)'''
    st.info(content)