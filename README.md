
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-30 15:00:00 EET+0200 2023-11-30 16:00:00 EET+0200               24.18
	          2 2023-11-30 15:00:00 EET+0200 2023-11-30 17:00:00 EET+0200              23.503
	          3 2023-11-30 15:00:00 EET+0200 2023-11-30 18:00:00 EET+0200           21.546667
	          4 2023-11-30 15:00:00 EET+0200 2023-11-30 19:00:00 EET+0200            20.18975

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-01 04:00:00 EET+0200 2023-12-01 05:00:00 EET+0200               8.549
	          2 2023-12-01 03:00:00 EET+0200 2023-12-01 05:00:00 EET+0200               8.552
	          3 2023-12-01 02:00:00 EET+0200 2023-12-01 05:00:00 EET+0200               8.597
	          4 2023-12-01 01:00:00 EET+0200 2023-12-01 05:00:00 EET+0200             8.70075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
