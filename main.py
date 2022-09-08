import pandas as pd
from pandas.io import gbq
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery


credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = bigquery.Client(credentials=credentials)

    

def main():
    st.title("Streamlit + BigQuery")
    file_upload = st.file_uploader("Upload a CSV file", type=["csv","txt","xlsx"])
    if file_upload:
        df = pd.read_csv(file_upload)
        table_id = 'Daily_sales_report.Big_Basket'
        job = client.load_table_from_dataframe(df, table_id)
        job.write_disposition = 'WRITE_TRUNCATE'
        job.result()



if __name__ == "__main__":
    main()
