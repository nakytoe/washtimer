
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-25 19:00:00 EET+0200 2023-11-25 20:00:00 EET+0200              15.335
	          2 2023-11-25 19:00:00 EET+0200 2023-11-25 21:00:00 EET+0200             15.3095
	          3 2023-11-25 18:00:00 EET+0200 2023-11-25 21:00:00 EET+0200              15.187
	          4 2023-11-25 18:00:00 EET+0200 2023-11-25 22:00:00 EET+0200             15.0365

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-24 15:00:00 EET+0200 2023-11-24 16:00:00 EET+0200               -50.0
	          2 2023-11-24 15:00:00 EET+0200 2023-11-24 17:00:00 EET+0200               -50.0
	          3 2023-11-24 15:00:00 EET+0200 2023-11-24 18:00:00 EET+0200               -50.0
	          4 2023-11-24 15:00:00 EET+0200 2023-11-24 19:00:00 EET+0200               -50.0


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
