
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-17 18:00:00 EET+0200 2024-01-17 19:00:00 EET+0200              16.919
	          2 2024-01-17 17:00:00 EET+0200 2024-01-17 19:00:00 EET+0200             16.1995
	          3 2024-01-17 16:00:00 EET+0200 2024-01-17 19:00:00 EET+0200              15.835
	          4 2024-01-17 16:00:00 EET+0200 2024-01-17 20:00:00 EET+0200             15.5965

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-18 04:00:00 EET+0200 2024-01-18 05:00:00 EET+0200               5.574
	          2 2024-01-18 03:00:00 EET+0200 2024-01-18 05:00:00 EET+0200               5.673
	          3 2024-01-18 03:00:00 EET+0200 2024-01-18 06:00:00 EET+0200               5.713
	          4 2024-01-18 02:00:00 EET+0200 2024-01-18 06:00:00 EET+0200             5.81175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
