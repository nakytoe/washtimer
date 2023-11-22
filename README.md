
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-22 08:00:00 EET+0200 2023-11-22 09:00:00 EET+0200               9.544
	          2 2023-11-22 07:00:00 EET+0200 2023-11-22 09:00:00 EET+0200               9.362
	          3 2023-11-22 07:00:00 EET+0200 2023-11-22 10:00:00 EET+0200            8.508333
	          4 2023-11-22 06:00:00 EET+0200 2023-11-22 10:00:00 EET+0200             7.71325

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-23 00:00:00 EET+0200 2023-11-23 01:00:00 EET+0200               1.473
	          2 2023-11-22 23:00:00 EET+0200 2023-11-23 01:00:00 EET+0200              1.5265
	          3 2023-11-22 22:00:00 EET+0200 2023-11-23 01:00:00 EET+0200            1.649333
	          4 2023-11-22 21:00:00 EET+0200 2023-11-23 01:00:00 EET+0200              1.7215


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
