
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-05 18:00:00 EET+0200 2023-11-05 19:00:00 EET+0200                6.02
	          2 2023-11-05 18:00:00 EET+0200 2023-11-05 20:00:00 EET+0200              5.9085
	          3 2023-11-05 18:00:00 EET+0200 2023-11-05 21:00:00 EET+0200            5.790667
	          4 2023-11-05 17:00:00 EET+0200 2023-11-05 21:00:00 EET+0200               5.649

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-05 02:00:00 EET+0200 2023-11-05 03:00:00 EET+0200               -0.01
	          2 2023-11-05 02:00:00 EET+0200 2023-11-05 04:00:00 EET+0200               -0.01
	          3 2023-11-05 02:00:00 EET+0200 2023-11-05 05:00:00 EET+0200               -0.01
	          4 2023-11-05 02:00:00 EET+0200 2023-11-05 06:00:00 EET+0200             -0.0095


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
