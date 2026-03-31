import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("PRODUCT SALES")
st.subheader("Sales by Category")
data={
    "Product":['Laptop','Shirt','Coffeemaker','Book','Headphones'],
    "category":['Electronics','Clothing','Appliances','Stationery','Electronics'],
    "Sales":[75000,2500,4200,600,3200]
}
df=pd.DataFrame(data)
filter_by_category=st.sidebar.selectbox("Filter by category",options=df['category'].unique())
filtered_data=df[df['category']==filter_by_category]
st.dataframe(filtered_data) 

st.line_chart(filtered_data.set_index('Product')['Sales'])