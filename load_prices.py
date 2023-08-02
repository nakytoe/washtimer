from washtimer import porssisahko as pool
import pandas as pd

# load data from sahkoporssi

if __name__ == "__main__":
    
    price_df = pool.request_latest_prices()

    price_df.to_csv("data/latest_prices.csv")


    