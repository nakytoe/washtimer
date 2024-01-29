
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-30 14:00:00 EET+0200 2024-01-30 15:00:00 EET+0200               3.032
	          2 2024-01-30 13:00:00 EET+0200 2024-01-30 15:00:00 EET+0200               3.027
	          3 2024-01-30 12:00:00 EET+0200 2024-01-30 15:00:00 EET+0200               3.025
	          4 2024-01-30 12:00:00 EET+0200 2024-01-30 16:00:00 EET+0200              3.0195

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-30 02:00:00 EET+0200 2024-01-30 03:00:00 EET+0200                 0.0
	          2 2024-01-30 02:00:00 EET+0200 2024-01-30 04:00:00 EET+0200                 0.0
	          3 2024-01-30 01:00:00 EET+0200 2024-01-30 04:00:00 EET+0200            0.000333
	          4 2024-01-30 01:00:00 EET+0200 2024-01-30 05:00:00 EET+0200              0.0005


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
