
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-10 16:00:00 EET+0200 2023-11-10 17:00:00 EET+0200                7.56
	          2 2023-11-10 15:00:00 EET+0200 2023-11-10 17:00:00 EET+0200                6.57
	          3 2023-11-10 15:00:00 EET+0200 2023-11-10 18:00:00 EET+0200            6.158667
	          4 2023-11-10 15:00:00 EET+0200 2023-11-10 19:00:00 EET+0200               5.953

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-11 00:00:00 EET+0200 2023-11-11 01:00:00 EET+0200               2.413
	          2 2023-11-11 00:00:00 EET+0200 2023-11-11 02:00:00 EET+0200              2.4585
	          3 2023-11-11 00:00:00 EET+0200 2023-11-11 03:00:00 EET+0200            2.476667
	          4 2023-11-11 00:00:00 EET+0200 2023-11-11 04:00:00 EET+0200             2.47775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
