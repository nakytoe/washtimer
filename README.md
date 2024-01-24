
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-24 08:00:00 EET+0200 2024-01-24 09:00:00 EET+0200              11.689
	          2 2024-01-24 10:00:00 EET+0200 2024-01-24 12:00:00 EET+0200             11.6125
	          3 2024-01-24 08:00:00 EET+0200 2024-01-24 11:00:00 EET+0200           11.604667
	          4 2024-01-24 10:00:00 EET+0200 2024-01-24 14:00:00 EET+0200             11.6025

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-25 00:00:00 EET+0200 2024-01-25 01:00:00 EET+0200               4.778
	          2 2024-01-24 23:00:00 EET+0200 2024-01-25 01:00:00 EET+0200               5.169
	          3 2024-01-24 22:00:00 EET+0200 2024-01-25 01:00:00 EET+0200               6.069
	          4 2024-01-24 21:00:00 EET+0200 2024-01-25 01:00:00 EET+0200              6.5665


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
