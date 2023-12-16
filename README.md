
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-16 17:00:00 EET+0200 2023-12-16 18:00:00 EET+0200               1.757
	          2 2023-12-16 17:00:00 EET+0200 2023-12-16 19:00:00 EET+0200              1.7345
	          3 2023-12-16 16:00:00 EET+0200 2023-12-16 19:00:00 EET+0200            1.725333
	          4 2023-12-16 15:00:00 EET+0200 2023-12-16 19:00:00 EET+0200               1.688

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-17 02:00:00 EET+0200 2023-12-17 03:00:00 EET+0200              -0.111
	          2 2023-12-17 02:00:00 EET+0200 2023-12-17 04:00:00 EET+0200              -0.111
	          3 2023-12-17 01:00:00 EET+0200 2023-12-17 04:00:00 EET+0200           -0.110667
	          4 2023-12-17 01:00:00 EET+0200 2023-12-17 05:00:00 EET+0200             -0.1105


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
