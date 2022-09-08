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
        tables = list(client.list_tables('Daily_sales_report'))
        table_names = [table.table_id for table in tables]
        if 'Big_Basket' in table_names:
            table_id_1 = 'Daily_sales_report.Big_Basket'
            job = client.update_table_from_dataframe(df, table_id_1)
        else:
            table_id_2 = 'Daily_sales_report.Big_Basket'
            job = client.load_table_from_dataframe(df, table_id_2)
        



if __name__ == "__main__":
    main()
