from StateData import *
import pandas as pd


def main():
    custmersData = pd.read_csv("Number_of_customer_accounts.csv")
    salesData = pd.read_csv("Retail_sales_of_electricity.csv")
    print(custmersData.to_string)
    typedCustomer = custmersData.convert_dtypes(infer_objects=True)
    print(typedCustomer.dtypes)

    # print(f"Costumers data has {custmersData.shape[1]} columns and {custmersData.shape[0]} rows")
    # print(f"Sales data has {salesData.shape[1]} columns and {salesData.shape[0]} rows")


if __name__ == "__main__":
    main()
