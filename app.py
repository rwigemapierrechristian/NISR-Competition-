import pandas as pd
import plotly.express as px
import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="LABOR FORCE DASHBOARD",
    page_icon=":bar_chart:",
    layout="wide"
)

# Load your data
df = pd.read_excel(
    io='RLFS Tables_ Annual_2022.xlsx',
    engine='openpyxl',
    sheet_name='Table 1',
    skiprows=1,
    usecols='A:H',
    nrows=8
)

df2 = pd.read_excel(
    io='RLFS Tables_ Annual_2022.xlsx',
    engine='openpyxl',
    sheet_name='Table 2-3',
    usecols='A:F',
    nrows=17
)

df3 = pd.read_excel(
    io='RLFS Tables_ Annual_2022.xlsx',
    engine='openpyxl',
    sheet_name='employed',
    usecols='A:H',
    nrows=15
)

df4 = pd.read_excel(
    io='RLFS Tables_ Annual_2022.xlsx',
    engine='openpyxl',
    sheet_name='Table 9-10',
    skiprows=14,
    usecols='A:G',
    nrows=48
)

df5 = pd.read_excel(
    io='RLFS Tables_ Annual_2022.xlsx',
    engine='openpyxl',
    sheet_name='Occupation',
    skiprows=18,
    usecols='A:G',
    nrows=9
)

# Calculate the required values
total_inactive_population = df.loc[4, 'Total']
total_inactive_males = df.loc[4, 'Male']
total_inactive_females = df.loc[4, 'Female']
employed_males = df.loc[5, 'Male']
employed_females = df.loc[5, 'Female']
unemployed_males = df.loc[6, 'Male']
unemployed_female = df.loc[6, 'Female']
outside_male = df.loc[7, 'Male']
outside_female = df.loc[7, 'Female']

# Create a DataFrame for the labor force pie chart
data_pie_labor = {
    'Category': ['Male', 'Female'],
    'Value': [total_inactive_males, total_inactive_females]
}

df_pie_labor = pd.DataFrame(data_pie_labor)

# Create a DataFrame for the employment/unemployment donut chart
data_donut_employment = {
    'Category': ['Employed (Male)', 'Employed (Female)', 'Unemployed (Male)', 'Unemployed (Female)'],
    'Value': [employed_males, employed_females, unemployed_males, unemployed_female]
}

df_donut_employment = pd.DataFrame(data_donut_employment)

# Create a DataFrame for the outside labor force bar chart
data_bar_outside = {
    'Category': ['Male', 'Female'],
    'Value': [outside_male, outside_female]
}

df_bar_outside = pd.DataFrame(data_bar_outside)

# Create a DataFrame for the area chart from df4 data
data_area_chart = {
    'Profession': df4['Profession'],
    'Value1': df4['Male'],
    'Value2': df4['Female'],
    'Value3': df4['Urban'],
    'Value4': df4['Rural'],
}

df_area_chart = pd.DataFrame(data_area_chart)

data_area_chart2 = {
    'Occupation': df5['Occupation'],
    'Value1': df5['Male'],
    'Value2': df5['Female'],
    'Value3': df5['Urban'],
    'Value4': df5['Rural'],
}
# Set custom colors
header_color = '#6CB4EE'
body_color = '#B9D9EB'
footer_color = '#041E42'
transparent_color = 'rgba(0, 0, 0, 0)'

# Add CSS styles for layout and colors
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {body_color};
        height: 100vh;
    }}
    .stPage {{
        background-color: {transparent_color};
    }}
    .stContent {{
        background-color: {transparent_color};
    }}
    .header {{
        position: fixed;
        top: 0;
        width: 100%;
        background-color: {header_color};
        text-align: center;
        padding: 20px 0;
        margin-left: -5rem;
        z-index: 1;
    }}
    .footer {{
        background-color: {footer_color};
        padding: 20px;
        text-align: center;
        margin-left:-5rem;
        margin-right:-5rem;
        margin-bottom:-30rem;
        color:white;
        margin-top: 5rem; /* Adjust margin to avoid overlapping content */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Create header
st.write(f"<div class='header'><h1>LABOUR FORCE 2022</h1></div>", unsafe_allow_html=True)
st.image("NISR.png", use_column_width=False, output_format='PNG', width=100)
# Create pie chart for labor force
fig_pie_labor = px.pie(
    df_pie_labor,
    values='Value',
    names='Category',
    title='Labor Force Distribution',
    color_discrete_map={'Male': footer_color, 'Female': footer_color}
)

# Create donut chart for employment and unemployment
fig_donut_employment = px.pie(
    df_donut_employment,
    values='Value',
    names='Category',
    title='Employment and Unemployment Rates',
    color_discrete_map={'Employed (Male)': footer_color, 'Employed (Female)': footer_color, 'Unemployed (Male)': footer_color, 'Unemployed (Female)': footer_color},
    hole=0.5  # Set the hole size to create a donut chart
)

# Create bar chart for outside labor force
fig_bar_outside = px.bar(
    df_bar_outside,
    x='Category',
    y='Value',
    title='Outside Labor Force Distribution',
    color='Category',
    labels={'Category': 'Gender', 'Value': 'Count'}
)

# Create line chart from df2 data
fig_line_chart1 = px.line(
    df2,
    x='Years',
    y=['Male', 'Female', 'Urban', 'Rural'],
    title='Population distribution by age',
    labels={'Category': 'Gender', 'Value': 'Count'}
)
# Set custom colors for the lines
colors = ['#6CB4EE', '#fff700', 'green', 'red']
for i, column in enumerate(['Male', 'Female', 'Urban', 'Rural']):
    fig_line_chart1.update_traces(line=dict(color=colors[i]), selector=dict(name=column))

# Create line chart from df3 data
fig_line_chart2 = px.line(
    df3,
    x='Years',
    y=['Male', 'Female', 'Urban', 'Rural'],
    title='Employment distribution by age',
    labels={'Category': 'Gender', 'Value': 'Count'}
)
# Set custom colors for the lines
for i, column in enumerate(['Male', 'Female', 'Urban', 'Rural']):
    fig_line_chart2.update_traces(line=dict(color=colors[i]), selector=dict(name=column))

# Create area chart from df4 data
fig_area_chart = px.area(
    df4,
    x= 'Profession',
    y= ['Male', 'Female', 'Urban', 'Rural'],
    title='Population distribution by occupation',
    labels={'Category': 'Gender', 'Value': 'Count'}
)
# Set custom colors for the areas
area_colors = ['blue', 'orange', 'green', 'red']
for i, column in enumerate(['Value1', 'Value2', 'Value3', 'Value4']):
    fig_area_chart.update_traces(line=dict(color=area_colors[i]), selector=dict(name=column))

# Create area chart from df4 data
fig_area_chart2 = px.area(
    df5,
    x= 'Occupation',
    y= ['Male', 'Female', 'Urban', 'Rural'],
    title='Population distribution by occupation with emphasis on managerial positions',
    labels={'Category': 'Gender', 'Value': 'Count'}
)
# Set custom colors for the areas
area_colors = ['blue', 'orange', 'green', 'red']
for i, column in enumerate(['Value1', 'Value2', 'Value3', 'Value4']):
    fig_area_chart.update_traces(line=dict(color=area_colors[i]), selector=dict(name=column))

# Reduce the size of the line charts to fit on a 14-inch screen
line_chart_width = 450
line_chart_height = 300
fig_line_chart1.update_layout(width=line_chart_width, height=line_chart_height)
fig_line_chart2.update_layout(width=line_chart_width, height=line_chart_height)

# Reduce the size of the area chart
area_chart_width = 600
area_chart_height = 300
fig_area_chart.update_layout(width=area_chart_width, height=area_chart_height)

# Reduce the size of the area chart
area_chart_width = 600
area_chart_height = 300
fig_area_chart2.update_layout(width=area_chart_width, height=area_chart_height)

# Make line chart backgrounds transparent
fig_line_chart1.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)
fig_line_chart2.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)
fig_area_chart.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)
fig_area_chart2.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)

# Make chart backgrounds transparent
fig_pie_labor.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)
fig_donut_employment.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)
fig_bar_outside.update_layout(plot_bgcolor=transparent_color, paper_bgcolor=transparent_color)

# Reduce the size of the other charts to fit on a 14-inch screen
chart_width = 300
chart_height = 300

fig_pie_labor.update_layout(width=chart_width, height=chart_height)
fig_donut_employment.update_layout(width=chart_width, height=chart_height)
fig_bar_outside.update_layout(width=chart_width, height=chart_height)

# Display the pie, donut, and bar charts side by side using st.columns
columns1 = st.columns(3)

with columns1[0]:
    st.plotly_chart(fig_pie_labor)

with columns1[1]:
    st.plotly_chart(fig_donut_employment)

with columns1[2]:
    st.plotly_chart(fig_bar_outside)

# Display the line charts side by side using st.columns
columns2 = st.columns(2)

with columns2[0]:
    st.plotly_chart(fig_line_chart1)

with columns2[1]:
    st.plotly_chart(fig_line_chart2)

# Display the area chart below the line charts
columns2 = st.columns(2)

with columns2[0]:
    st.plotly_chart(fig_area_chart)

with columns2[1]:
    st.plotly_chart(fig_area_chart2)


# Create footer
st.image("logo.svg", use_column_width=False, output_format='SVG', width=100)
st.write(f"<div class='footer'><p>NISR COMPETITION 2023<p> </br> <p>https://www.statistics.gov.rw/publication/1919</p>", unsafe_allow_html=True)
