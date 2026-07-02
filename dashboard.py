import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime


st.set_page_config(
    page_title="PlaceMux Executive Dashboard",
    layout="wide"
)


df = pd.read_csv("data/customer_data_cleaned.csv")
df['segment'] = df['segment'].replace({'Sme': 'SME'})


st.title("PlaceMux — Executive Dashboard")
st.caption(f"Data last refreshed from: customer_data_cleaned.csv | Loaded at: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
st.markdown("---")

st.sidebar.header("Filters")

# Segment filter
all_segments = ['All'] + sorted(df['segment'].unique().tolist())
selected_segment = st.sidebar.selectbox("Segment", all_segments)

# City filter
all_cities = ['All'] + sorted(df['city'].unique().tolist())
selected_city = st.sidebar.selectbox("City", all_cities)

# Apply filters
filtered_df = df.copy()
if selected_segment != 'All':
    filtered_df = filtered_df[filtered_df['segment'] == selected_segment]
if selected_city != 'All':
    filtered_df = filtered_df[filtered_df['city'] == selected_city]

st.sidebar.markdown("---")
st.sidebar.caption(f"Showing {len(filtered_df)} of {len(df)} customers")

st.subheader("Key Metrics")

# Row 1: Three KPI tiles side by side
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Customers",
        value=len(filtered_df),
        help="Row count after deduplication. Note: customer_id has known reuse issues (Task 2)."
    )

with col2:
    st.metric(
        label="Avg Purchase Amount",
        value=f"₹{filtered_df['purchase_amount'].mean():,.0f}",
        help="Mean purchase amount across selected customers."
    )

with col3:
    st.metric(
        label="Avg Satisfaction Score",
        value=f"{filtered_df['satisfaction_score'].mean():.2f} / 5",
        help="Mean satisfaction score (1-5 scale). Overall baseline: 2.89."
    )

st.markdown("---")

# Row 2: Two charts side by side
col4, col5 = st.columns(2)

with col4:
    st.subheader("Avg Purchase Amount by Segment")
    seg_data = filtered_df.groupby('segment')['purchase_amount'].mean().reset_index()
    seg_data.columns = ['Segment', 'Avg Purchase Amount']
    overall_avg = filtered_df['purchase_amount'].mean()
    fig1 = px.bar(seg_data, x='Segment', y='Avg Purchase Amount',
                  title="vs Overall Average: ₹{:,.0f}".format(overall_avg))
    fig1.add_hline(y=overall_avg, line_dash="dash", line_color="red",
                   annotation_text="Overall avg")
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.subheader("Avg Satisfaction by Segment")
    sat_data = filtered_df.groupby('segment')['satisfaction_score'].mean().reset_index()
    sat_data.columns = ['Segment', 'Avg Satisfaction']
    fig2 = px.bar(sat_data, x='Segment', y='Avg Satisfaction',
                  title="Scale: 1-5")
    fig2.update_yaxes(range=[0, 5])
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Row 3: Two more charts
col6, col7 = st.columns(2)

with col6:
    st.subheader("Avg Purchase Amount by City")
    city_data = filtered_df.groupby('city')['purchase_amount'].mean().reset_index()
    city_data.columns = ['City', 'Avg Purchase Amount']
    city_data = city_data.sort_values('Avg Purchase Amount', ascending=True)
    fig3 = px.bar(city_data, x='Avg Purchase Amount', y='City',
                  orientation='h', title="Ranked by spend")
    st.plotly_chart(fig3, use_container_width=True)

with col7:
    st.subheader("Customers by Signup Year")
    year_data = filtered_df.groupby('signup_year')['customer_id'].count().reset_index()
    year_data.columns = ['Year', 'Customer Count']
    fig4 = px.line(year_data, x='Year', y='Customer Count',
                   markers=True, title="New customers per year")
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.caption("Built by [Your Name] | PlaceMux Phase 1 | Data: customer_data_cleaned.csv")

