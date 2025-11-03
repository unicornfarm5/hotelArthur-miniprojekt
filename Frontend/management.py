import streamlit as st
import plotly.graph_objects as go


def vis_management_side():
    st.title("Management View")
    st.write("Her er management-delen af systemet.")

    # Example graph specific to management view
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 3, 2, 5, 4]))
    st.plotly_chart(fig, config={"scrollZoom": False})

    # Tilføj mere indhold her – grafer, billeder, tabeller osv.
    st.image ("OverviewGraf.png", caption="Overview Grafik")