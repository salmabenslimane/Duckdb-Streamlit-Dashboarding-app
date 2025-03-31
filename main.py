import streamlit as st
import duckdb
import pandas as pd

# Set page configuration
st.set_page_config(page_title="OLAP Dashboard", layout="wide")


# Title of the app
st.title("OLAP Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
csv_file = st.sidebar.file_uploader("📂 Importer un fichier CSV", type=["csv"])
delimiter = st.sidebar.selectbox("Sélecteur de délimiteur", options=[",", ";", "|"])


if csv_file: 
    # Read the CSV file into a DataFrame using the selected delimiter so you can run a request with it 
    df = pd.read_csv(csv_file, delimiter=delimiter)
    
    # Display the DataFrame in the app
    st.subheader("DataFrame")
    st.write(df)

    # Create a DuckDB connection
    # This will create an in-memory database
    con = duckdb.connect()

    #create views orders from the dataframe
    con.execute("""
                CREATE OR REPLACE VIEW orders AS 
                SELECT * FROM df
    """)

    # Execute a sample query to show the data
    query = "SELECT * FROM orders LIMIT 10"
    result = con.execute(query).fetchdf()
    st.subheader("Sample Query Result")
    st.write(result)

