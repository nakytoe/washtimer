
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-08 15:00:00 EET+0200 2024-01-08 16:00:00 EET+0200              20.733
	          2 2024-01-08 15:00:00 EET+0200 2024-01-08 17:00:00 EET+0200             20.4425
	          3 2024-01-08 15:00:00 EET+0200 2024-01-08 18:00:00 EET+0200           18.998667
	          4 2024-01-08 15:00:00 EET+0200 2024-01-08 19:00:00 EET+0200             18.3505

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-09 04:00:00 EET+0200 2024-01-09 05:00:00 EET+0200               3.257
	          2 2024-01-09 03:00:00 EET+0200 2024-01-09 05:00:00 EET+0200               3.261
	          3 2024-01-09 02:00:00 EET+0200 2024-01-09 05:00:00 EET+0200               3.279
	          4 2024-01-09 02:00:00 EET+0200 2024-01-09 06:00:00 EET+0200              3.2925


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
