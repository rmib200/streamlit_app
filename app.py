import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
PAGE_CONFIG={"page_title":"Colab APP", "page_icon":":smiley:", "layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)

file1 = "countries-continent.csv"
file2 = "country-GDP.csv"
file3 = "country-population.csv"
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
# df2.rename(columns={"GDP per capita":"GDP"}, errors="raise")
df2.rename(columns={df2.columns[1]:"GDP"}, inplace=True)
df2["GDP"] = df2["GDP"].str.replace("$","")
df2["GDP"] = df2["GDP"].str.replace(",","").astype(int)
data = pd.merge(df1,df2)
data = pd.merge(data,df3)

def main():
  st.title("Streamlit app")
  st.subheader("Table data Country-Subregion")
  st.write(df1)
  st.subheader("Table data Country-GDP")
  st.write(df2)
  st.subheader("Table data Country-Population")
  st.write(df3)
  st.write(df2.columns[1])
  st.subheader("Table data Merged")
  st.write(data)
  menu=["Home", "About"]
  choice = st.sidebar.selectbox("Menu",menu)
  if choice == "Home":
    st.subheader("st for colab")

if __name__ == "__main__":
  main()