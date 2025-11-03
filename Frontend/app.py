import streamlit as st
from management import vis_management_side

# Baggrundsfarve (lys beige)
st.markdown("""
    <style>
    .stApp {
        background-color: #f4efeb;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo Titel med farve (HTML)
st.markdown("<h1 style='color:#a66a0a;'>Hotel Kong Arthur</h1>", unsafe_allow_html=True)

# Sidebar-menu med kun to valg
st.sidebar.title("Navigation")
valg = st.sidebar.radio("Vælg en side:", ["Forside", "Management"])

# Forside
if valg == "Forside":
    st.markdown("<h2 style='color:#a66a0a;'>Hotel Kong Arthur Management System</h2>", unsafe_allow_html=True)
    st.write("Velkommen til forsiden!")

# Management-side
elif valg == "Management":
    vis_management_side()
