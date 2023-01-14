# import libraries
import streamlit as st
import plotly.express as px

# set heading of the webpage
st.header("SIP Calculator")

# create input boxes to take the inputs from the user/frontend
# get the monthly amount
monthly_amount = st.number_input('Monthly Investment', value=500)
# get the expected yearly return
yearly_return = st.number_input('Expected return rate (p.a)', value=15)
# get the time period of the investment
time_period = st.number_input('Time period', value=10)

# get monthly return rate
monthly_return = yearly_return/12/100
# get total number of months
total_months = time_period * 12
# get expected return rate
expected_return = monthly_amount * ((((1 + monthly_return)**(total_months))-1)
                                    * (1 + monthly_return))/monthly_return

# create 2 grid columns
first_col, second_col = st.columns(2)
# show invested amount
first_col.subheader(f'Invested amount is: \
    {round(monthly_amount*total_months)}')
# show expected return amount
second_col.subheader(f'Expected return is: {round(expected_return)}')

# make donut chart
labels = ['Invested amount', 'Expected return']
# set values
values = [round(monthly_amount*total_months), round(expected_return)]
fig = px.pie(labels, values=values, names=labels, hole=0.6)
# show chart
st.plotly_chart(fig)
