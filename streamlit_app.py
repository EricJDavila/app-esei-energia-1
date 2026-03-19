import streamlit as st
import pandas as pd

st.title("🎈 Esta es mi nueva aplicación")
st.write(
    "Hola mundo!."
)

 
df = pd.DataFrame({'dia': [1, 2, 3, 4], 'demanda': [20, 30, 15, 35]})
st.line_chart(df)


