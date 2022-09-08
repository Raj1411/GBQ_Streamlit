import pandas as pd
from pandas.io import gbq
import streamlit as st


def main():
    st.title("Streamlit + BigQuery")
    file_upload = st.file_uploader("Upload a CSV file", type=["csv","txt","xlsx"])
    if file_upload:
         if file_upload.type == "text/csv":
            df = pd.read_csv(file_upload)
            df.to_gbq(destination_table="Daily_sales_report.Big_Basket", project_id="crafty-hook-331815", if_exists="append")
         else:
            df = pd.read_excel(file_upload)
            df.to_gbq(destination_table="Daily_sales_report.Big_Basket", project_id="crafty-hook-331815", if_exists="append")


# df = pd.read_csv("D:\Office\Flipkart & FBF\Python\Sales data to Big Query\manufacturer_sales-report-gamma_01-09-2022_08-09-2022_1662614157.39.csv")
# df.to_gbq(destination_table="Daily_sales_report.Big_Basket", project_id="crafty-hook-331815", if_exists="append")




if __name__ == "__main__":
    main()
