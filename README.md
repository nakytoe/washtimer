
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-16 18:00:00 EET+0200 2024-01-16 19:00:00 EET+0200               21.18
	          2 2024-01-16 17:00:00 EET+0200 2024-01-16 19:00:00 EET+0200              21.135
	          3 2024-01-16 17:00:00 EET+0200 2024-01-16 20:00:00 EET+0200               20.89
	          4 2024-01-16 16:00:00 EET+0200 2024-01-16 20:00:00 EET+0200             20.5085

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-18 00:00:00 EET+0200 2024-01-18 01:00:00 EET+0200               8.432
	          2 2024-01-17 23:00:00 EET+0200 2024-01-18 01:00:00 EET+0200              9.8805
	          3 2024-01-17 02:00:00 EET+0200 2024-01-17 05:00:00 EET+0200              10.269
	          4 2024-01-17 02:00:00 EET+0200 2024-01-17 06:00:00 EET+0200             10.4935


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
