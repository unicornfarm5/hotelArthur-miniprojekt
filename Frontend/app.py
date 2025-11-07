import streamlit as st
from PIL import Image

from management import vis_management_side
from styling import use_styling

st.header("Hotel Kong Arthur")
st.divider()

# Sidebar-menu
st.sidebar.title("Navigation")
image = Image.open("kongArthurLogo.png")
st.sidebar.image(image, width=120)
valg = st.sidebar.radio("Vælg en side:", ["Forside", "Graf overblik"])

# Forside
if valg == "Forside":
    st.markdown("<h2 >Hotel Kong Arthur Management System</h2>", unsafe_allow_html=True)
    st.write("Ingen nye beskeder")

# Management-side
elif valg == "Graf overblik":
    vis_management_side()

image = Image.open("kongArthurLogo.png")

# CSS
use_styling()