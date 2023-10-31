
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-10-31 15:00:00 EET+0200 2023-10-31 16:00:00 EET+0200               7.497
	          2 2023-10-31 15:00:00 EET+0200 2023-10-31 17:00:00 EET+0200              6.7805
	          3 2023-10-31 15:00:00 EET+0200 2023-10-31 18:00:00 EET+0200            6.208333
	          4 2023-10-31 15:00:00 EET+0200 2023-10-31 19:00:00 EET+0200               5.489

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-01 03:00:00 EET+0200 2023-11-01 04:00:00 EET+0200               0.001
	          2 2023-11-01 03:00:00 EET+0200 2023-11-01 05:00:00 EET+0200               0.001
	          3 2023-11-01 02:00:00 EET+0200 2023-11-01 05:00:00 EET+0200            0.028333
	          4 2023-11-01 02:00:00 EET+0200 2023-11-01 06:00:00 EET+0200             0.07575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
