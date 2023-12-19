
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-20 18:00:00 EET+0200 2023-12-20 19:00:00 EET+0200               10.19
	          2 2023-12-20 18:00:00 EET+0200 2023-12-20 20:00:00 EET+0200             10.0505
	          3 2023-12-20 18:00:00 EET+0200 2023-12-20 21:00:00 EET+0200              10.015
	          4 2023-12-20 17:00:00 EET+0200 2023-12-20 21:00:00 EET+0200             9.92575

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-20 03:00:00 EET+0200 2023-12-20 04:00:00 EET+0200                 0.0
	          2 2023-12-20 02:00:00 EET+0200 2023-12-20 04:00:00 EET+0200              0.0005
	          3 2023-12-20 01:00:00 EET+0200 2023-12-20 04:00:00 EET+0200            0.000667
	          4 2023-12-20 01:00:00 EET+0200 2023-12-20 05:00:00 EET+0200             0.00075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
