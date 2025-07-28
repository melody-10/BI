# BI/Modules/Utils/header.py

import streamlit as st

def show_header(text_title: str):
    # Layout: logo + title side by side
    col1, col2 = st.columns([1, 6])
    
    with col1:
        st.image("assets/UP logo.jpg", width=200)
        
    with col2:
        st.title(text_title)
        st.caption("📘 Developed for: *Business Intelligence (Graduate Level)*")
        st.caption("Instructor: Edgar Avalos-Gauna (2025), Universidad Panamericana")
        st.caption("📊 Dataset Source: [Yelp Academic Dataset](https://business.yelp.com/data/resources/open-dataset/)")
