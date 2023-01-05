# to install all the dependencies
# pip install streamlit pandas yfinance plotly

import streamlit as st
import pandas as pd
import yfinance as yf
from plotly import graph_objs as go
from datetime import date, timedelta


st.title("Personal Stock Dashboard")

# today's date
today = date.today()
# one month back date
one_month_back_date = today - timedelta(weeks=4)

# text input field
ticker = st.text_input("Ticker Name", placeholder="AAPL", value="AAPL")

# make two(bootstrap) columns so that we can place date fields in a single line on the frontend
col1, col2 = st.columns([1, 1])

# date input field
with col1:
    start_date = st.date_input("Start Date", one_month_back_date)
# date input field
with col2:
    end_date = st.date_input("End Date")

# hide the index from the streamlit table
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)


def get_data_and_make_chart():

    """
    function to scrape stock data and create stock chart
    """

    # create loader
    data_load_state = st.text("Loading data...")

    # get stock data
    df = yf.download(tickers=ticker, start=start_date, end=end_date)
    # reset dataframe index and change date column type
    df.reset_index(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    # reverse dataframe
    df = df.iloc[::-1]

    # create chart
    if not df.empty:
        st.table(data=df)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["Date"], y=df["Open"]))
        fig.layout.update(
            title_text=f"Stock Chart for {ticker}",
            xaxis_title="Date",
            yaxis_title="Stock Price",
            xaxis_rangeslider_visible=True,
        )
        st.plotly_chart(fig)
        data_load_state.text("Loading data... done!")

    # stock data not found
    else:
        st.write("Nothing to display. Please check the ticker name")

    return


# run the function
if __name__ == "__main__":
    get_data_and_make_chart()
