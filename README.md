
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-11 19:00:00 EET+0200 2024-03-11 20:00:00 EET+0200              12.452
	          2 2024-03-11 18:00:00 EET+0200 2024-03-11 20:00:00 EET+0200             11.8595
	          3 2024-03-11 18:00:00 EET+0200 2024-03-11 21:00:00 EET+0200           11.209667
	          4 2024-03-11 17:00:00 EET+0200 2024-03-11 21:00:00 EET+0200            10.85675

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-11 02:00:00 EET+0200 2024-03-11 03:00:00 EET+0200               4.204
	          2 2024-03-11 02:00:00 EET+0200 2024-03-11 04:00:00 EET+0200               4.262
	          3 2024-03-11 02:00:00 EET+0200 2024-03-11 05:00:00 EET+0200               4.288
	          4 2024-03-11 01:00:00 EET+0200 2024-03-11 05:00:00 EET+0200               4.353


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
