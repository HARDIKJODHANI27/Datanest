# PYTHON LIBRARIES IMPORTS
import streamlit as st
from app.utils.file_loader import load_file
import pandas as pd

# ANALYTICS IMPORTS
from app.analytics.profiler import profile_dataframe, profile_columns
from app.analytics.data_quality import check_data_quality
from app.analytics.numerical_statistics import numeric_statistics
from app.analytics.categorical_statistics import categorical_statistics



# ---------- HOME PAGE ----------

def show_home():
    st.header("Welcome to Datanest")

    st.write(
        "Your data analysis workspace."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Datasets", 3)
    col2.metric("Total Rows", "24,580")
    col3.metric("Analyses", 12)
    col4.metric("Reports", 5)

    st.subheader("Recent Datasets")

    recent_datasets = {
        "Dataset": [
            "Sales",
            "Customers",
            "Transactions"
        ],
        "Source": [
            "Excel",
            "CSV",
            "Tally"
        ],
        "Rows": [
            12450,
            8320,
            3810
        ],
        "Status": [
            "Ready",
            "Ready",
            "Processing"
        ]
    }

    st.dataframe(
        recent_datasets,
        use_container_width=True,
        hide_index=True
    )
# ---------- UPLOAD PAGE ----------

def show_upload():
    st.header("Upload Data")

    st.write(
        "Upload a CSV or Excel file to explore your data."
    )

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["csv", "xlsx", "xls"]
    )

    if uploaded_file is not None:
        st.success(
            f"{uploaded_file.name} uploaded successfully!"
        )

        try:
            df = load_file(uploaded_file)
            st.session_state["df"] = df

            st.subheader("Data Preview")

            st.dataframe(
                df.head(10),
                use_container_width=True,
                hide_index=True
            )

            st.subheader("Data Profile")
            profile = profile_dataframe(df)

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Rows", profile["row_count"])
            col2.metric("Columns", profile["column_count"])
            col3.metric("Missing Values", profile["missing_values"])
            col4.metric("Duplicate Rows", profile["duplicate_rows"])

            st.subheader("Column Profile")
            column_profiles = profile_columns(df)

            st.dataframe(column_profiles, use_container_width=True, hide_index=True)



        except Exception as e:
            st.error(
                f"Unable to process the file: {e}"
            )





#------------- SHOW REPORTS ---------------
def show_reports():
    st.header("Show Reports")


#------------- SHOW ANALYSIS ---------------
def show_analysis():
    st.header("Show Analysis")

    num_stats = numeric_statistics(df)
    cat_stats = categorical_statistics(df)


    if "df" not in st.session_state:
        st.info("Please Upload a dataset first!")
        return

    df = st.session_state["df"]
    quality = check_data_quality(df)

    st.subheader("Data Quality")
    col1, col2 = st.columns(2)

    col1.metric("Missing Values", quality["missing_values"])
    col2.metric("Duplicate Rows", quality["duplicate_rows"])

    if quality["empty_columns"]:
        st.warning(
            f"Completely empty columns: {', '.join(quality["empty_columns"])}"
        )

    else:
        st.success("No completely empty columns")


    if quality["missing_columns"]:
        st.warning("Missing values by columns:")

        missing_df = pd.DataFrame(
            list(quality["missing_columns"].items()),
            columns=["Column", "Missing Values"]
        )

        st.dataframe(
            missing_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("No missing values found!")

    st.subheader("Numeric Statistics")

    if num_stats:
        num_stats.df = pd.DataFrame(num_stats)

        st.dataframe(
            num_stats.df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No numeric data found in the dataset!")    

    st.subheader("Categorical Statistics")

    if cat_stats:
        categorical_df = pd.DataFrame(cat_stats)

        st.dataframe(
            categorical_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No categorical columns found in the dataset.")


#------------- SHOW DATASET ---------------
def show_datasets():
    st.header("Show Datasets")
# ---------- PAGE NAVIGATION ----------

def run_app():

    st.set_page_config(
        page_title="Datanest",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Datanest")

    st.write(
        "Your data. Your insights."
    )

    st.write(
        "An intelligent business analytics platform "
        "for importing, analyzing, visualizing, and understanding data."
    )

    st.sidebar.title("Datanest")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Upload Data",
            "Datasets",
            "Analysis",
            "Reports"
        ]
    )

    if page == "Home":
        show_home()

    elif page == "Upload Data":
        show_upload()

    elif page == "Datasets":
        show_datasets()

    elif page == "Analysis":
        show_analysis()

    elif page == "Reports":
        show_reports()