
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-28 08:00:00 EET+0200 2024-01-28 09:00:00 EET+0200               2.326
	          2 2024-01-28 11:00:00 EET+0200 2024-01-28 13:00:00 EET+0200               2.317
	          3 2024-01-28 10:00:00 EET+0200 2024-01-28 13:00:00 EET+0200               2.316
	          4 2024-01-28 08:00:00 EET+0200 2024-01-28 12:00:00 EET+0200             2.31275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-29 00:00:00 EET+0200 2024-01-29 01:00:00 EET+0200              -0.031
	          2 2024-01-28 23:00:00 EET+0200 2024-01-29 01:00:00 EET+0200              -0.016
	          3 2024-01-28 22:00:00 EET+0200 2024-01-29 01:00:00 EET+0200           -0.010333
	          4 2024-01-28 21:00:00 EET+0200 2024-01-29 01:00:00 EET+0200             -0.0075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
