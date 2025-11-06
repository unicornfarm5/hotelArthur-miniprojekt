import pandas as pd
import streamlit as st

#### GRAF 1 ###
    #får data fra excel filen
    #viser hele databasen - kan søges i på ui
    #ide fra 
    #https://www.youtube.com/watch?v=yg0Y7w4AHhw
st.title("Booking overblik")
st.subheader("Bookings 2024 fuldt overblik")

@st.cache_data
def load_data(path: str):
    data = pd.read_excel(path)
    return data

from pathlib import Path   
excel_df = load_data(Path(__file__).parent / "../DataService/data.xlsx")

st.dataframe(excel_df)


### GRAF 2 ###
    #også blot udfra excel
    #indtjening fordelt på lande
    #ide fra 
    #https://www.youtube.com/watch?v=yg0Y7w4AHhw
import plotly.express as px

st.divider()
st.subheader("Indtjening fordelt på lande")
def graf_two():
    data = excel_df
    st.bar_chart(data, x="Country", y="Price")

graf_two()



### API
import requests

st.divider()
st.header("Grafer hentet med API er herunder")
st.subheader("Indtjening fordelt på lande")


        #viewmodel (eller ihvert fald ikke frontend)
@st.cache_data
def load_data():
    r = requests.get("http://localhost:5000/data")
    return pd.DataFrame(r.json())
api_df = load_data()

### graf 3 ###
st.write("Data fra API overview:")
st.dataframe(api_df)
st.divider()

### graf 4 ###
# Plot med Plotly
fig = px.bar(api_df, x="Country", y="Price", title="Indtjening fordelt på lande (API)")
st.plotly_chart(fig)




