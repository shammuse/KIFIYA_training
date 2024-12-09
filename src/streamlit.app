import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simple Dashboard", layout="wide")

with st.sidebar:
    selected_option = st.radio("Select an option:", [1, 2])

st.title("Simple Streamlit Dashboard")


if selected_option == 1:
    st.header("Option 1: Upload CSV and Plot Data")

    uploaded_file = st.file_uploader("Choose a CSV file to upload", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("Uploaded Data Preview")
        st.dataframe(data.head())

        st.subheader("Graph of Uploaded Data")

        if st.checkbox("Show Plot"):
            if data.shape[1] >= 2: 
                x_col = st.selectbox("Select X-axis column", data.columns)
                y_col = st.selectbox("Select Y-axis column", data.columns)

                fig, ax = plt.subplots(figsize=(8, 2))
                ax.plot(data[x_col], data[y_col], marker='o', color='b')
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"{y_col} vs {x_col}")
                st.pyplot(fig)
            else:
                st.warning("Uploaded data must have at least two columns for plotting.")
    else:
        st.warning("Please upload a CSV file to display and plot the data.")


elif selected_option == 2:
    st.header("Display Sample Data and Plot")

    st.subheader("Sample Data Preview")
    sample_data = {
        "Month": ["January", "February", "March", "April", "May", "June"],
        "Sales": [250, 300, 450, 200, 500, 400]
    }
    df = pd.DataFrame(sample_data)
    st.dataframe(df)

    st.subheader("Sample Data Plot")
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.plot(df["Month"], df["Sales"], marker='o', color='green')
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Monthly Sales")
    st.pyplot(fig)

    st.markdown("<h6 style='text-align: center;'>Dashboard Development 📊 using Streamlit</h6>", unsafe_allow_html=True)
