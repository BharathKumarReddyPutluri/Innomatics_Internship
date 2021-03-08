import streamlit as st

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset_loc = "Data/train.csv"
image_loc = "image/classification.png"


@st.cache
def load_data(dataset_loc):
    df = pd.read_csv(dataset_loc)
    return df


def load_description(df):
        # Preview of the dataset
        st.header("Data Preview")
        preview = st.radio("Choose Head/Tail?", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

        # display the whole dataset
        if(st.checkbox("Show complete Dataset")):
            st.write(df)

        # Show shape
        if(st.checkbox("Display the shape")):
            st.write(df.shape)
            dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
            if(dim == "Rows"):
                st.write("Number of Rows", df.shape[0])
            if(dim == "Columns"):
                st.write("Number of Columns", df.shape[1])

        # show columns
        if(st.checkbox("Show the Columns")):
            st.write(df.columns)

def load_viz(df):
        st.header("Data Visualisation")
        st.subheader("Seaborn - countplot")
        fig = plt.figure()
        sns.countplot(x='output', data=df)
        st.pyplot(fig)


def main():

    # Title/ text
    st.title('Simple Classification')
    st.image(image_loc, use_column_width = True)

    # loading the data
    df = load_data(dataset_loc)

    # display description
    load_description(df)

    #visualis
    load_viz(df)


if(__name__ == '__main__'):
    main()
