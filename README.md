
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-03 19:00:00 EET+0200 2023-12-03 20:00:00 EET+0200              16.395
	          2 2023-12-03 18:00:00 EET+0200 2023-12-03 20:00:00 EET+0200              16.364
	          3 2023-12-03 18:00:00 EET+0200 2023-12-03 21:00:00 EET+0200           16.120333
	          4 2023-12-03 17:00:00 EET+0200 2023-12-03 21:00:00 EET+0200             15.9715

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-03 07:00:00 EET+0200 2023-12-03 08:00:00 EET+0200              11.019
	          2 2023-12-03 06:00:00 EET+0200 2023-12-03 08:00:00 EET+0200             11.0595
	          3 2023-12-03 06:00:00 EET+0200 2023-12-03 09:00:00 EET+0200              11.181
	          4 2023-12-03 06:00:00 EET+0200 2023-12-03 10:00:00 EET+0200            11.39325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
