
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-06 17:00:00 EET+0200 2024-01-06 18:00:00 EET+0200              37.199
	          2 2024-01-06 17:00:00 EET+0200 2024-01-06 19:00:00 EET+0200             33.7555
	          3 2024-01-06 16:00:00 EET+0200 2024-01-06 19:00:00 EET+0200           30.770333
	          4 2024-01-06 16:00:00 EET+0200 2024-01-06 20:00:00 EET+0200            29.27775

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-08 00:00:00 EET+0200 2024-01-08 01:00:00 EET+0200                7.77
	          2 2024-01-07 23:00:00 EET+0200 2024-01-08 01:00:00 EET+0200               9.243
	          3 2024-01-07 22:00:00 EET+0200 2024-01-08 01:00:00 EET+0200           10.018667
	          4 2024-01-07 21:00:00 EET+0200 2024-01-08 01:00:00 EET+0200            10.23775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
