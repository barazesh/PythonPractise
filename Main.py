from StateData import *
import pandas as pd


def main():
    sectorNames = ["all", "residential", "commercial",
                   "industrial", "transportation", "other"]
    customersData = pd.read_csv("Number_of_customer_accounts.csv")
    headers = customersData.columns
    salesData = pd.read_csv("Retail_sales_of_electricity.csv")
    print(customersData.shape)
    States = []
    for state in range(0, 62):
        snapshotData = []

        for d in range(3, len(headers)):
            sectorData = []

            for s in range(0, 4):
                i = state*7+s+1
                customers = int(customersData.iloc[i, d])
                sale = int(salesData.iloc[i, d])
                # try:
                #     customers = int(customersData.iloc[state*7+s+2, d])
                #     sale = int(salesData.iloc[state*7+s+1, d])
                # except ValueError as ex:
                #     print(ex.__traceback__)

                sectorTemp = Sector(
                    name=sectorNames[s], customers=customers, sales=sale)
                sectorData.append(sectorTemp)

            snapTemp = Snapshot(date=str(headers[d]), sectorsData=sectorData)
            snapshotData.append(snapTemp)

        tempState = State(
            name=str(customersData.iloc[state*7, 0]), snapshots=snapshotData)
        States.append(tempState)

    print("Finished")


if __name__ == "__main__":
    main()
