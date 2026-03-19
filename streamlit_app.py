import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

st.title("Título de la aplicación")

st.markdown("**Una aplicación**")


df = pd.DataFrame(rng(0).standard_normal((200, 3)), columns=["a", "b", "c"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)

# df = pd.DataFrame({'demanda 1': [10, 26, 13, 28], 'demanda 2': [20, 30, 15, 35]})
# st.line_chart(df)
