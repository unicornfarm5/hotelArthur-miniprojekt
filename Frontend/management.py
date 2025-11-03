import streamlit as st
import plotly.graph_objects as go

def vis_management_side():
    # Tilføj baggrundsfarve og overskriftfarve via CSS
    st.markdown("""
        <style>
        .stApp {
            background-color: #f4efeb;
        }
        h1, h2 {
            color: #a66a0a;
        }
        </style>
        """, unsafe_allow_html=True)

    # Overskrift med brun farve
    st.markdown("<h1 style='color:#a66a0a;'>Management View</h1>", unsafe_allow_html=True)
    st.write("Her er management-delen af systemet.")

    # Graf med brun farve
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4],
        mode='lines+markers',
        line=dict(color='#a66a0a', width=3),
        marker=dict(color='#a66a0a', size=8)
    ))
    fig.update_layout(
        plot_bgcolor='#f4efeb',
        paper_bgcolor='#f4efeb',
        font=dict(color='#a66a0a')
    )
    st.plotly_chart(fig, config={"scrollZoom": False})

    # Billede
    st.image("OverviewGraf.png", caption="Overview Grafik")