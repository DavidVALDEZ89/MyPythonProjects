#Source link https://github.com/Sven-Bo/streamlit-sales-dashboard

#MODULES
import pandas as pd  #we need pandas for dataframes,  pip install pandas
import plotly.express as px  #we need ploty for graphs, pip install plotly-express
import streamlit as st  #we need streamlit for visualisation, pip install streamlit

#View
st.set_page_config(
    page_title="Sales Dashboard", #Web page title
    page_icon=":bar_chart:", #Web page icon
    layout="wide")  #Web page layout

@st.cache
def get_data_from_excel():  #strores information in the cache
    #DATA IMPORT
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000)

    # st.dataframe(df)  #returns the dataframe

    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour  #Adds 'hour" column to dataframe 24hr format
    return df

df = get_data_from_excel()

#SIDEBAR

#Filter setup
#FILTER HEADER
st.sidebar.header("Filter data")

#FILTER
city = st.sidebar.multiselect(  #Variable defirnition
    "By City:",  #Title of the filter
    options=df["City"].unique(),  #Column to filter
    default=df["City"].unique()  #Set default value to all
)

#FILTER
customer_type = st.sidebar.multiselect(  #Variable defirnition
    "By Customer type:",  #Title of the filter
    options=df["Customer_type"].unique(),  #Column to filter
    default=df["Customer_type"].unique()  #Set default value to all
)

#FILTER
gender = st.sidebar.multiselect(  #Variable defirnition
    "By Gender:",  #Title of the filter
    options=df["Gender"].unique(),  #Column to filter
    default=df["Gender"].unique()  #Set default value to all
)

#FILTER
payment = st.sidebar.multiselect(  #Variable defirnition
    "By Payment method:",  #Title of the filter
    options=df["Payment"].unique(),  #Column to filter
    default=df["Payment"].unique()  #Set default value to all
)

#Filtered information
df_filtered_data = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender & Payment == @payment"
)

#MAINPAGE
st.title("Sales Dashboard")
st.markdown("##")

#KPI
sales_total = int(df_filtered_data["Total"].sum())  #return the sum of the total column
rating_average = round(df_filtered_data["Rating"].mean(),1)  #returns the average rating
rating_star = ":star:" * int(round(rating_average,0))
sales_by_transaction_average = round(df_filtered_data["Total"].mean(),2)

column_1, column_2, column_3 = st.columns(3)
with column_1:
    st.subheader("Total Sales:")
    st.subheader(f"US ${sales_total:,}")
with column_2:
    st.subheader("Average Rating:")
    st.subheader(f"{rating_average} {rating_star}")
with column_3:
    st.subheader("Average sales per transaction")
    st.subheader(f"US ${sales_by_transaction_average:,}")
    
    
st.markdown("---")

#Chart
sales_by_product_line = (
    df_filtered_data.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)

sales_by_product_line_chart = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line Chart</b>",
    color_discrete_sequence=["#3783A1"] * len(sales_by_product_line),
    template="plotly_white",
)

sales_by_product_line_chart.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#Chart
sales_by_hour = (
    df_filtered_data.groupby(by=["hour"]).sum()[["Total"]]
)

sales_by_hour_chart = px.line(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour Chart</b>",
    color_discrete_sequence=["#3783A1"] * len(sales_by_product_line),
    template="plotly_white",
)

sales_by_hour_chart.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

column_1, column_2 = st.columns(2)  #arrange charts next to each other
column_1.plotly_chart(sales_by_product_line_chart, use_container_width=True)
column_2.plotly_chart(sales_by_hour_chart, use_container_width=True)

#Hide streamlit style
st_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style> 
"""

st.markdown(st_style, unsafe_allow_html=True)

st.dataframe(df_filtered_data)  #returns the dataframe