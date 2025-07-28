from Modules.Utils.load_data import load_dataset

df = load_dataset("Data/yelp_sampled_df.parquet")
st.dataframe(df.head())
