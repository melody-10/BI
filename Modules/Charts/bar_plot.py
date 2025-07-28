import plotly.express as px


def bar_plotly(data):
    try:
        bar_fig = px.bar(
            x=data.index,
            y=data.values,
            labels={'x': 'Category', 'y': 'Count'},
            title="Composition of Selected Business Categories"
        )
        st.plotly_chart(bar_fig, use_container_width=True)
    except:
        st.info("Select one or more categories to see their frequency in the chart.")
