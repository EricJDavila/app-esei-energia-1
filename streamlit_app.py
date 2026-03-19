import streamlit as st
import pandas as pd

st.title("🎈 Esta es mi nueva aplicación")
st.write(
    "Hola mundo!."
)

 
df = pd.DataFrame({'demanda 1': [10, 26, 13, 28], 'demanda 2': [20, 30, 15, 35]})
st.line_chart(df)


