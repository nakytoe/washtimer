
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-17 07:00:00 EET+0200 2024-01-17 08:00:00 EET+0200                18.6
	          2 2024-01-17 07:00:00 EET+0200 2024-01-17 09:00:00 EET+0200             18.4585
	          3 2024-01-17 06:00:00 EET+0200 2024-01-17 09:00:00 EET+0200           17.868333
	          4 2024-01-17 06:00:00 EET+0200 2024-01-17 10:00:00 EET+0200            17.18375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-18 00:00:00 EET+0200 2024-01-18 01:00:00 EET+0200               8.432
	          2 2024-01-17 23:00:00 EET+0200 2024-01-18 01:00:00 EET+0200              9.8805
	          3 2024-01-17 22:00:00 EET+0200 2024-01-18 01:00:00 EET+0200           10.617333
	          4 2024-01-17 21:00:00 EET+0200 2024-01-18 01:00:00 EET+0200              11.268


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
