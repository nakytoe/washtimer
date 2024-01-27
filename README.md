
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-27 18:00:00 EET+0200 2024-01-27 19:00:00 EET+0200               2.563
	          2 2024-01-27 18:00:00 EET+0200 2024-01-27 20:00:00 EET+0200               2.547
	          3 2024-01-27 17:00:00 EET+0200 2024-01-27 20:00:00 EET+0200            2.538333
	          4 2024-01-27 16:00:00 EET+0200 2024-01-27 20:00:00 EET+0200               2.529

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-29 00:00:00 EET+0200 2024-01-29 01:00:00 EET+0200              -0.031
	          2 2024-01-28 23:00:00 EET+0200 2024-01-29 01:00:00 EET+0200              -0.016
	          3 2024-01-28 22:00:00 EET+0200 2024-01-29 01:00:00 EET+0200           -0.010333
	          4 2024-01-28 21:00:00 EET+0200 2024-01-29 01:00:00 EET+0200             -0.0075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
