import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from cath import api_df
from styling import use_styling

def vis_management_side():
    #CSS
    use_styling() 

    # Overskrift med brun farve
    st.title("Management View")
    st.write("Her er management-only, hvor du kan se grafer og data over hotellets performance.")

    # Billede fra Tableau
    st.image("OverviewGraf.png", caption="Overview Grafik")
    st.divider()
    
    st.text("Grafer fresh fra databsasen over API")
    st.title("Booking overblik")

    #graf 1 - tabel
    st.dataframe(api_df)
    st.divider()

    st.title("Økonomi overblik")
    #graf 2 - søjlediagram
    graph1 = px.bar(api_df, x="Country", y="Price", title="Indtjening fordelt på lande", color="Price", color_continuous_scale=px.colors.sequential.Oranges,
                    labels ={'Price':'Omsætning', 'Country':''})
    st.plotly_chart(graph1)

    #graf 3 - indtjenin på værelsestype efter sæson
    graph2 = px.bar(api_df, x="Price", y="Room Type", title="Indtjening på værelsestype efter sæson", orientation='h', # horisontal bar chart
                    labels={'Price':'Omsætning', 'Room Type':'Værelsestype'},
                    color="Season",
                    color_discrete_map={
                        'low':'goldenrod',
                        'mid':'sandybrown',
                        'high':'darkorange'})
    st.plotly_chart(graph2)

    #graf 4 
    graph3 = px.bar(api_df, x='Days Rented', y='Country', 
                          title='Længde af ophold fordelt på lande', 
                          color='Days Rented', color_continuous_scale=px.colors.sequential.Oranges,
                          labels={'Days Rented':'Total ophold i dage', 'Country':''})
    st.plotly_chart(graph3)
    

   
