import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Retail Predictive Analytics",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    


# 👇 YAHAN LOGIN FUNCTION AAYEGA

def login_page():

    st.markdown("""
    <h1 style='text-align:center;color:#38BDF8;'>
        🛍️ Retail Analytics Dashboard
    </h1>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("### 🔐 Login")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("🚀 Login"):

            if username == "admin" and password == "admin123":

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error(
                    "Invalid Username or Password"
                )


    st.markdown("""
<style>
...

    /* Whole App */

    .stApp {
        background: linear-gradient(
            135deg,
            #020617,
            #0F172A,
            #111827
        );
        color: white;
        overflow-x: hidden;
    }

    /* Main */

    .main {
        background-color: transparent;
    }

    /* Dashboard Title */

    h1 {
        color: #38BDF8 !important;
        text-align: center;
        font-size: 58px !important;
        font-weight: 900 !important;
        margin-bottom: 35px;

        text-shadow:
            0px 0px 18px rgba(56,189,248,0.8);

        animation: fadeDown 1s ease;
    }

    /* Section Headers */

    h2, h3 {
        color: #FACC15 !important;
        font-weight: 800 !important;

        animation: fadeInUp 1s ease;
    }

    /* Sidebar */

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            to bottom,
            #172554,
            #1E3A8A
        );

        border-right: 1px solid rgba(255,255,255,0.1);
        if st.sidebar.button("🔄 Refresh Dashboard"):
    st.success("Dashboard Refreshed Successfully")
    }

    /* Sidebar Text */

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Metric Cards */

    div[data-testid="stMetric"] {

        background: linear-gradient(
            135deg,
            #2563EB,
            #7C3AED
        );

        padding: 22px;

        border-radius: 22px;

        border: 1px solid rgba(255,255,255,0.1);

        box-shadow:
            0 8px 24px rgba(0,0,0,0.45);

        transition: 0.4s;

        animation: fadeInUp 1s ease;
    }

    div[data-testid="stMetric"]:hover {

        transform:
            translateY(-6px)
            scale(1.02);

        box-shadow:
            0 14px 30px rgba(59,130,246,0.5);
    }

    /* Metric Labels */

    div[data-testid="stMetricLabel"] {
        color: #E0F2FE !important;
        font-weight: 700;
    }

    /* Metric Values */

   div[data-testid="stMetric"]:hover {

    transform:
        translateY(-10px)
        scale(1.03);

    box-shadow:
        0 18px 35px rgba(59,130,246,0.7);
}

    /* Selectbox */

    div[data-baseweb="select"] {

        background-color: black !important;

        border-radius: 14px;

        border: 1px solid #38BDF8;

        transition: 0.3s;
    }

    div[data-baseweb="select"]:hover {
        border: 1px solid #FACC15;
    }

    /* Selectbox Text */

    div[data-baseweb="select"] span {
        color: white !important;
    }

    /* Dropdown Menu */

    ul {
        background-color: black !important;
        color: white !important;
    }

    /* Download Button */

    .stDownloadButton button {

        background: black !important;

        color: white !important;

        border: 1px solid #38BDF8;

        border-radius: 14px;

        padding: 10px 20px;

        font-weight: bold;

        transition: 0.3s;

        animation: fadeInUp 1s ease;
    }

    .stDownloadButton button:hover {

        background: #2563EB !important;

        transform: scale(1.05);

        border: 1px solid #FACC15;
    }

    /* Dataframe */

    .stDataFrame {

        border-radius: 16px;

        overflow: hidden;

        animation: fadeUp 1.2s ease-in-out;
    }

    /* Graph Containers */

    .element-container {

        animation: fadeUp 1.2s ease-in-out;
    }

    /* Smooth Page Animation */

    section.main > div {

        animation: fadeUp 1s ease-in-out;

        transition: 0.4s ease-in-out;
    }

    section.main > div:hover {

    transform:
        translateY(-6px)
        scale(1.01);

    transition: 0.4s ease-in-out;
}

    /* Fade Up Animation */

    @keyframes fadeUp {

        from {
            opacity: 0;
            transform: translateY(40px);
        }

        to {
            opacity: 1;
            transform: translateY(0px);
        }
    }

    /* Fade Down Animation */

    @keyframes fadeDown {

        from {
            opacity: 0;
            transform: translateY(-40px);
        }

        to {
            opacity: 1;
            transform: translateY(0px);
        }
    }
    div[data-baseweb="select"]:focus {

    outline: none !important;

    box-shadow:
        0 0 10px rgba(56,189,248,0.8) !important;
}



/* Blue Theme Hover */

*:focus,
button:focus,
input:focus,
textarea:focus,
select:focus {

    outline: none !important;

    border-color: #38BDF8 !important;

    box-shadow:
        0 0 10px rgba(56,189,248,0.8) !important;
}

/* Selectbox Hover */

div[data-baseweb="select"]:hover {

    border: 1px solid #38BDF8 !important;

    box-shadow:
        0 0 10px rgba(56,189,248,0.5);
}
/* Active Tab Blue Color */

button[data-baseweb="tab"] {

    color: white !important;

    background-color: transparent !important;
}

button[data-baseweb="tab"][aria-selected="true"] {

    color: #38BDF8 !important;


    background-color: rgba(56,189,248,0.15) !important;
}



    </style>
    """,
    unsafe_allow_html=True
)
st.title("🛍️ Retail Predictive Analytics Dashboard")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Sales",
    "👥 Customers",
    "🤖 Forecast",
    "📦 Inventory"
])

# Load dataset
df = pd.read_csv("data_clean.csv")
# Sidebar Filter


st.sidebar.title("Filters")
st.sidebar.markdown(
    """
    <div style="
        background-color:black;
        padding:15px;
        border-radius:12px;
        border:1px solid #38BDF8;
        text-align:center;
        font-weight:bold;
        color:white;
    ">
        Retail Analytics Filters
    </div>
    """,
    unsafe_allow_html=True
)

selected_country = st.sidebar.selectbox(
    "Select Country",
    df['Country'].unique()
)
filtered_df = df[
    df['Country'] == selected_country
]


# Download Dataset

csv = filtered_df.to_csv(index=False)

st.sidebar.download_button(
    label="⬇ Download Dataset",
    data=csv,
    file_name="clean_retail_data.csv",
    mime="text/csv"
)
st.sidebar.markdown("---")

st.sidebar.subheader("Dataset Info")

st.sidebar.write(
    f"Rows: {len(filtered_df):,}"
)

st.sidebar.write(
    f"Countries: {df['Country'].nunique()}"
)

st.sidebar.write(
    f"Products: {df['Description'].nunique()}"
)



with tab1:

    # KPI

    total_revenue = filtered_df['Revenue'].sum()

    total_orders = filtered_df['InvoiceNo'].nunique()

    total_customers = filtered_df['CustomerID'].nunique()

    # KPI Display

    col1, col2, col3 = st.columns(3)
  
    col1.metric(
        "Total Revenue",
        f"${total_revenue:,.2f}"
    )

    col2.metric(
        "Total Orders",
        total_orders
    )

    col3.metric(
        "Total Customers",
        total_customers
    )
    # Revenue Trend

    st.subheader("📈 Revenue Trend")

    filtered_df['InvoiceDate'] = pd.to_datetime(
        filtered_df['InvoiceDate']
    )

    monthly = (
        filtered_df.groupby(
            filtered_df['InvoiceDate'].dt.to_period('M')
        )['Revenue']
        .sum()
        .reset_index()
    )

    monthly['InvoiceDate'] = monthly[
        'InvoiceDate'
    ].astype(str)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        monthly['InvoiceDate'],
        monthly['Revenue'],
        marker='o',
        linewidth=4,
        color='#38BDF8',
        markersize=10
    )

    ax.set_facecolor("#111827")

    fig.patch.set_facecolor("#111827")

    ax.tick_params(colors='white')

    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.grid(
        True,
        alpha=0.3,
        color='white'
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

     # Top Products

    st.subheader("🛒 Top Products")

    top_products = (
    filtered_df.groupby('Description')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

    fig2, ax2 = plt.subplots(figsize=(10,5))

    top_products.sort_values().plot(
    kind='barh',
    ax=ax2,
    color='#38BDF8'
)

    ax2.set_facecolor("#111827")

    fig2.patch.set_facecolor("#111827")

    ax2.tick_params(colors='white')

    ax2.spines['bottom'].set_color('white')
    ax2.spines['left'].set_color('white')

    ax2.set_title(
    "Top Revenue Generating Products",
    color='white'
)

    ax2.grid(
    True,
    alpha=0.3,
    color='white'
)

    st.pyplot(fig2)


with tab2:

    # Customer Churn Analysis
    st.subheader("👥 Overall Customer Churn Analysis")

    rfm = pd.read_csv("rfm_features.csv")
    st.write(rfm.columns)
 
    churn_count = (
    rfm['Churned']
    .value_counts()
    .reindex([0, 1], fill_value=0)
)
    fig6, ax6 = plt.subplots(figsize=(5,5))
    ax6.pie(
        churn_count.values,
        labels=['Active', 'Churned'],
        autopct='%1.1f%%',
        colors=['#38BDF8', '#FACC15'],
        textprops={'color': 'white'}
    )

    ax6.set_facecolor("#111827")
    fig6.patch.set_facecolor("#111827")

    st.pyplot(fig6)

    rfm_filtered = rfm
    st.subheader("📌 Customer Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", len(rfm_filtered))

    col2.metric(
    "Champions",
    (rfm_filtered["Segment"] == "Champion").sum()
)
    col3.metric(
    "Loyal Customers",
    (rfm_filtered["Segment"] == "Loyal Customer").sum()
)
    col4.metric(
    "At Risk",
    (rfm_filtered["Segment"] == "At Risk").sum()
)
    # Dataset Preview
    st.write(rfm.columns)
    st.subheader("📄 Dataset Preview")

    st.dataframe(
       filtered_df.head(10)
    )

    # RFM Analysis

    st.subheader("📊 RFM Analysis")

    rfm_filtered = rfm[
    rfm['Country'] == selected_country
]

    rfm_preview = rfm_filtered[
    ['CustomerID', 'Recency', 'Frequency', 'Monetary']
].head(10)

    st.dataframe(rfm_preview)
    st.subheader("👥 Customer Segmentation")

    segment_counts = rfm_filtered['Segment'].value_counts()

    fig_seg, ax_seg = plt.subplots(figsize=(8,4))

    segment_counts.plot(
    kind='bar',
    ax=ax_seg
)

    ax_seg.set_title("Customer Segments")
    ax_seg.set_xlabel("Segment")
    ax_seg.set_ylabel("Number of Customers")

    st.pyplot(fig_seg)

    st.subheader("👑 Top 10 Customers by Revenue")

    top_customers = (
    filtered_df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

    st.subheader("🛒 Top 10 Products")

    top_products = (
    filtered_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

    st.bar_chart(top_products)

    st.dataframe(top_customers)

   
with tab3:

    # Forecast Section

    st.subheader("🤖 Overall Revenue Forecast")

    daily = pd.read_csv(
        "daily_demand.csv"
    )

    daily['InvoiceDate'] = pd.to_datetime(
        daily['InvoiceDate']
    )

    fig3, ax3 = plt.subplots(figsize=(12,5))

    ax3.plot(
        daily['InvoiceDate'],
        daily['total_revenue'],
        color='#38BDF8',
        linewidth=3
    )

    ax3.set_facecolor("#111827")

    fig3.patch.set_facecolor("#111827")

    ax3.tick_params(colors='white')

    ax3.spines['bottom'].set_color('white')

    ax3.spines['left'].set_color('white')

    ax3.grid(
        True,
        alpha=0.3,
        color='white'
    )

    st.pyplot(fig3)

    # Forecast Metrics

    st.subheader("📊 Forecast Metrics")

    st.write("MAE:", "Forecast Model")

    st.write("RMSE:", "Forecast Model")

    st.write("R² Score:", "Forecast Model")

    # Country-wise Revenue

    st.subheader("🌍 Country-wise Revenue")

    country_rev = (
        filtered_df.groupby('Country')['Revenue']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig4, ax4 = plt.subplots(figsize=(10,5))

    country_rev.sort_values().plot(
        kind='barh',
        ax=ax4,
        color='#FACC15'
    )

    ax4.set_facecolor("#111827")

    fig4.patch.set_facecolor("#111827")

    ax4.tick_params(colors='white')

    ax4.spines['bottom'].set_color('white')

    ax4.spines['left'].set_color('white')

    ax4.grid(
        True,
        alpha=0.3,
        color='white'
    )

    st.pyplot(fig4)


    with tab4:
      top_moving = (
    filtered_df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

      st.subheader("🚀 Fast Moving Products")
      st.bar_chart(top_moving)

    # Inventory Optimization

      st.subheader("📦 Inventory Optimization")

      top_inventory = (
        filtered_df.groupby('Description')['Quantity']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

      fig7, ax7 = plt.subplots(figsize=(10,5))

      top_inventory.sort_values().plot(
        kind='barh',
        ax=ax7,
        color='#38BDF8'
    )

      ax7.set_facecolor("#111827")

      fig7.patch.set_facecolor("#111827")

      ax7.tick_params(colors='white')

      ax7.spines['bottom'].set_color('white')

      ax7.spines['left'].set_color('white')

      ax7.grid(
        True,
        alpha=0.3,
        color='white'
    )

      st.pyplot(fig7)

    # Download Clean Dataset

      st.subheader("⬇ Download Clean Dataset")

      csv = filtered_df.to_csv(index=False)

      st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="clean_retail_data.csv",
        mime="text/csv"
    )
      


# Project Summary

    st.subheader("📌 Project Summary")

    st.write("""
This Retail Predictive Analytics Dashboard helps analyze:

#Sales Performance
#Customer Churn Analysis
#RFM Customer Segmentation
#Top Customers
#Top Products
#Revenue Forecasting
#Fast Moving Products
#Inventory Optimization
#Country-wise Insights

using Machine Learning and Data Analytics.
""")