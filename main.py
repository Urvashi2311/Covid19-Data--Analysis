
import streamlit as st
import pandas as pd
import preprocessor
import plotly.express as px



df = pd.read_csv('worldometer_data.csv')
day_wise_df = pd.read_csv('day_wise.csv')
country_wise_df =pd.read_csv('full_grouped.csv')

df = preprocessor.preprocess_df(df)

country_wise_df = preprocessor.preprocess_country(country_wise_df)

st.sidebar.title("Covid19 Analysis")
st.sidebar.image('covid-19-image.png')

user_menu = st.sidebar.radio(
    'Select an Option',
    ( 'Overall Analysis', 'Country-wise Analysis')
)

if user_menu == 'Overall Analysis':

    ccases_over_time = day_wise_df[day_wise_df.columns[:2]]
    fig1 = px.line(ccases_over_time, x="Date", y="Confirmed")
    st.title("World Daily Confirmed Cases")
    st.plotly_chart(fig1)

    dcases_over_time = day_wise_df[['Date', 'Deaths']]
    fig2 = px.line(dcases_over_time, x="Date", y="Deaths")
    st.title("World Daily Death Cases")
    st.plotly_chart(fig2)

    rcases_over_time = day_wise_df[['Date', 'Recovered']]
    fig3 = px.line(rcases_over_time, x="Date", y="Recovered")
    st.title("World Daily Recovered Cases")
    st.plotly_chart(fig3)

    st.table(df)


if user_menu == 'Country-wise Analysis':
    st.sidebar.header("Country-wise Analysis")

    country_list = country_wise_df['Country/Region'].unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country', country_list)

    sd = country_wise_df
    sd = sd[(sd['Country/Region'] == selected_country)]

    death_df = sd[["Date", "Deaths"]]

    fig = px.line(sd, x="Date", y=["Confirmed", "Deaths", "Recovered"])
    st.title(selected_country + " Overall Analysis")
    st.plotly_chart(fig)

    st.table(sd)











