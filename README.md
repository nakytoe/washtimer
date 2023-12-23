
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-23 18:00:00 EET+0200 2023-12-23 19:00:00 EET+0200               8.245
	          2 2023-12-23 18:00:00 EET+0200 2023-12-23 20:00:00 EET+0200              8.2215
	          3 2023-12-23 18:00:00 EET+0200 2023-12-23 21:00:00 EET+0200               8.025
	          4 2023-12-23 17:00:00 EET+0200 2023-12-23 21:00:00 EET+0200             7.81825

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-25 00:00:00 EET+0200 2023-12-25 01:00:00 EET+0200               2.926
	          2 2023-12-24 23:00:00 EET+0200 2023-12-25 01:00:00 EET+0200                3.26
	          3 2023-12-24 22:00:00 EET+0200 2023-12-25 01:00:00 EET+0200               3.413
	          4 2023-12-24 21:00:00 EET+0200 2023-12-25 01:00:00 EET+0200              3.4895


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
