
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-21 14:00:00 EET+0200 2024-03-21 15:00:00 EET+0200              16.498
	          2 2024-03-21 13:00:00 EET+0200 2024-03-21 15:00:00 EET+0200              16.252
	          3 2024-03-21 12:00:00 EET+0200 2024-03-21 15:00:00 EET+0200           16.168667
	          4 2024-03-21 11:00:00 EET+0200 2024-03-21 15:00:00 EET+0200            14.37125

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-22 00:00:00 EET+0200 2024-03-22 01:00:00 EET+0200               5.086
	          2 2024-03-21 23:00:00 EET+0200 2024-03-22 01:00:00 EET+0200               6.233
	          3 2024-03-21 22:00:00 EET+0200 2024-03-22 01:00:00 EET+0200            6.902333
	          4 2024-03-21 21:00:00 EET+0200 2024-03-22 01:00:00 EET+0200               7.716


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
