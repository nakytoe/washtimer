
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-04 08:00:00 EET+0200 2024-01-04 09:00:00 EET+0200              47.027
	          2 2024-01-04 07:00:00 EET+0200 2024-01-04 09:00:00 EET+0200             42.1135
	          3 2024-01-04 07:00:00 EET+0200 2024-01-04 10:00:00 EET+0200           40.475333
	          4 2024-01-04 08:00:00 EET+0200 2024-01-04 12:00:00 EET+0200            39.65875

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-04 00:00:00 EET+0200 2024-01-04 01:00:00 EET+0200               7.242
	          2 2024-01-03 23:00:00 EET+0200 2024-01-04 01:00:00 EET+0200               9.013
	          3 2024-01-03 22:00:00 EET+0200 2024-01-04 01:00:00 EET+0200               10.14
	          4 2024-01-03 21:00:00 EET+0200 2024-01-04 01:00:00 EET+0200             10.2655


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
