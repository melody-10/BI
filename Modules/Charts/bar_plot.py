import plotly.express as px
import streamlit as st


def bar_plotly(data):
    bar_fig = px.bar(
        x=data.index,
        y=data.values,
        labels={'x': 'Category', 'y': 'Count'},
        title="Composition of Selected Business Categories"
    )
    st.plotly_chart(bar_fig, use_container_width=True)
