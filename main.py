import datetime as dt
import pandas as pd
import numpy as np
import pytz
from washtimer import porssisahko as pool
from washtimer.consumption import calculate_consumption, min_max_hours

## calculate 

if __name__ == "__main__":

    tz = pytz.timezone(pool.TIMEZONE)

    def convert_to_timezone(time_str: str, tz = tz)->str:
        fmt1 = "%Y-%m-%dT%H:%M:%S.000Z"
        t = dt.datetime.strptime(time_str, fmt1)
        t_tz = tz.localize(t)
        fmt2 = "%Y-%m-%d %H:%M:%S %Z%z"
        return dt.datetime.strftime(t_tz, fmt2)
    
    price_df = None

    try: # read file if exists
        with open("data/latest_prices.csv", "r") as f:
            price_df = pd.read_csv("data/latest_prices.csv")
    except FileNotFoundError:
        price_df = pool.request_latest_prices()

    # calculate cheapest and most expensive hours
    min_max_df = min_max_hours(price_df)

    # convert timezones
    min_max_df.start_time = min_max_df.start_time.apply(convert_to_timezone)
    min_max_df.end_time = min_max_df.end_time.apply(convert_to_timezone)

    md_base = """
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

"""
    
    for power_hour, g in min_max_df.groupby("power_hours"):
        desc1 = f"""For {power_hour}h program:"""
        for _, row in g.iterrows():
            kind = "cheapest" if row.minmax == "min" else "expensive"
            price = np.round(row.mean_price, 2)
            start = row.start_time
            end = row.end_time
            desc2 = f"""
    it is the most {kind} ({price} €c/kWh on avg) to set the timer:
        - to begin at {start}, or 
        - to end at {end}

"""
            desc1 += desc2
        md_base += desc1

    print(md_base)
    