import streamlit as st
from management import vis_management_side

# Baggrundsfarve og logo-positionering
st.markdown("""
    <style>
    .stApp {
        background-color: #f4efeb;
    }
    .logo {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 1;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo i øverste højre hjørne
st.markdown('<div class="logo"><img src="kongArthurLogo.jpg" width="120"></div>', unsafe_allow_html=True)

# Titel med farve
st.markdown("<h1 style='color:#a66a0a;'>Hotel Kong Arthur</h1>", unsafe_allow_html=True)

# Sidebar-menu
st.sidebar.title("Navigation")
valg = st.sidebar.radio("Vælg en side:", ["Forside", "Management"])

# Forside
if valg == "Forside":
    st.markdown("<h2 style='color:#a66a0a;'>Hotel Kong Arthur Management System</h2>", unsafe_allow_html=True)
    st.write("Velkommen til forsiden!")

# Management-side
elif valg == "Management":
    vis_management_side()