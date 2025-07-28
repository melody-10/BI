import io

# Button to download filtered results as CSV
csv_buffer = io.StringIO()
filtered_df.to_csv(csv_buffer, index=False)
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv_buffer.getvalue(),
    file_name=f"filtered_yelp_{selected_state}.csv",
    mime="text/csv"
)
