
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-29 18:00:00 EET+0200 2023-11-29 19:00:00 EET+0200                31.0
	          2 2023-11-29 18:00:00 EET+0200 2023-11-29 20:00:00 EET+0200                31.0
	          3 2023-11-29 17:00:00 EET+0200 2023-11-29 20:00:00 EET+0200           28.933333
	          4 2023-11-30 09:00:00 EET+0200 2023-11-30 13:00:00 EET+0200            27.96925

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-01 00:00:00 EET+0200 2023-12-01 01:00:00 EET+0200               9.041
	          2 2023-11-30 23:00:00 EET+0200 2023-12-01 01:00:00 EET+0200             10.2985
	          3 2023-11-30 22:00:00 EET+0200 2023-12-01 01:00:00 EET+0200              11.412
	          4 2023-11-30 21:00:00 EET+0200 2023-12-01 01:00:00 EET+0200             11.5255


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
