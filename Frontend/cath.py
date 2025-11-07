import pandas as pd
import streamlit as st
import requests
import time
import plotly.express as px


st.title("Booking overblik")

st.divider()
st.header("Grafer hentet med API er herunder")
st.subheader("Indtjening fordelt på lande")


        #viewmodel (eller ihvert fald ikke frontend)
@st.cache_data
def load_data():
    r = requests.get("http://dataservice:5000/data")
    #kode fra chatgpt
    for i in range(5):  # prøv op til 5 gange
        try:
            r = requests.get("http://dataservice:5000/data")
            return pd.DataFrame(r.json())
        except requests.exceptions.RequestException:
            print("Backend ikke klar, prøver igen om 2 sekunder...")
            time.sleep(2)
    raise RuntimeError("Kunne ikke hente data fra backend")

api_df = load_data()

### graf 3 ###
st.write("Data fra API overview:")
st.dataframe(api_df)
st.divider()

### graf 4 ###
# Plot med Plotly
fig = px.bar(api_df, x="Country", y="Price", title="Indtjening fordelt på lande (API)")
st.plotly_chart(fig)




