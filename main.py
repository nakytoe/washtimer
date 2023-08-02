import datetime as dt
import pandas as pd
import numpy as np
import pytz
from washtimer import porssisahko as pool
from washtimer.consumption import calculate_consumption, min_max_hours

## calculate cheapest and most expensive hours to use appliance


BASE_TEXT = """
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

"""

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
    df = min_max_hours(price_df)

    # convert timezones
    df.start_time = df.start_time.apply(convert_to_timezone)
    df.end_time = df.end_time.apply(convert_to_timezone)

    df.sort_values(by = "power_hours", inplace= True)
    df = df[["power_hours", "start_time", "end_time", "mean_price", "minmax"]]

    df = df.rename({"mean_price":"mean price [€c/kWh]",
                "power_hours":"program duration [h]",
                "start_time":"start time",
                "end_time":"end time"}, axis = 1)
    
    out = BASE_TEXT

    for minmax, g in df.groupby("minmax"):
        out += f"The {minmax} prices for today:\n\n"
        s = g.drop("minmax", axis = 1).to_string(index=False)
        out += f"{s}\n\n"

    print(out)
    
    with open("README.md", "w") as f:
        f.write(out)
    