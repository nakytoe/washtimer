
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-20 17:00:00 EET+0200 2024-01-20 18:00:00 EET+0200              12.649
	          2 2024-01-20 10:00:00 EET+0200 2024-01-20 12:00:00 EET+0200             12.3735
	          3 2024-01-20 17:00:00 EET+0200 2024-01-20 20:00:00 EET+0200           12.421667
	          4 2024-01-20 16:00:00 EET+0200 2024-01-20 20:00:00 EET+0200             12.2885

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-21 00:00:00 EET+0200 2024-01-21 01:00:00 EET+0200               8.307
	          2 2024-01-20 23:00:00 EET+0200 2024-01-21 01:00:00 EET+0200              8.5195
	          3 2024-01-20 22:00:00 EET+0200 2024-01-21 01:00:00 EET+0200               8.713
	          4 2024-01-20 21:00:00 EET+0200 2024-01-21 01:00:00 EET+0200             9.01475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
