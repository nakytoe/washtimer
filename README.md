
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-20 10:00:00 EET+0200 2023-11-20 11:00:00 EET+0200              19.841
	          2 2023-11-20 16:00:00 EET+0200 2023-11-20 18:00:00 EET+0200             19.0725
	          3 2023-11-20 16:00:00 EET+0200 2023-11-20 19:00:00 EET+0200              18.791
	          4 2023-11-20 16:00:00 EET+0200 2023-11-20 20:00:00 EET+0200            18.43275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-20 03:00:00 EET+0200 2023-11-20 04:00:00 EET+0200               7.429
	          2 2023-11-20 03:00:00 EET+0200 2023-11-20 05:00:00 EET+0200              7.4365
	          3 2023-11-20 02:00:00 EET+0200 2023-11-20 05:00:00 EET+0200            7.548333
	          4 2023-11-20 02:00:00 EET+0200 2023-11-20 06:00:00 EET+0200             7.66875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
