import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("my first streamlit app")
data=pd.read_csv("https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv")
st.subheader("Raw data")
st.write("this is a scatter chart ")
st.sidebar.header("filter otions")
selected_category=st.sidebar.selectbox("Select Category",options=['All','Adelie','Gentoo','Chinstrap'])
filtered_data=data[data['species']==selected_category]
if selected_category!='All':
    filtered_data=data[data['species']==selected_category]
    st.scatter_chart(filtered_data,x='flipper_length_mm',y='body_mass_g',color='species')
else:
    st.scatter_chart(data,x='flipper_length_mm',y='body_mass_g',color='sex')

# seaborn
plot= sns.histplot(filtered_data,x='culmen_length_mm',kde=True)
st.pyplot(plot.figure)
