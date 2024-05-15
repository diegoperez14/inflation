import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Constants
FRED_API_KEY = 'e19f1d72a9499db392c6c07299482c26'
FRED_URL = 'https://api.stlouisfed.org/fred/series/observations'
SERIES_ID = 'CPIAUCSL'  # Consumer Price Index for All Urban Consumers: All Items

# Function to get data from FRED
def get_inflation_data(api_key, series_id):
    params = {
        'api_key': api_key,
        'series_id': series_id,
        'file_type': 'json'
    }
    response = requests.get(FRED_URL, params=params)
    data = response.json()
    observations = data['observations']
    df = pd.DataFrame(observations)
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].astype(float)
    return df

# Main Streamlit app
def main():
    st.title("Historical Inflation Data")
    
    # Load data
    st.write("Fetching data from FRED...")
    df = get_inflation_data(FRED_API_KEY, SERIES_ID)
    
    st.write("Data fetched successfully!")
    
    # Display data
    st.write("### Inflation Data", df)
    
    # Plot data
    st.write("### Inflation Rate Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['value'], label='CPI')
    ax.set_xlabel('Date')
    ax.set_ylabel('CPI')
    ax.set_title('Consumer Price Index Over Time')
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
