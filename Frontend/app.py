import streamlit as st

st.title("Hotel Kong Arthur Management System")

st.sidebar.header("Hop mellem views")


st.text("Her er en graf")
#fra https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config = {'scrollZoom': False})


#Vi kan bruge denne
#https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart
#til at lave et kort yay
