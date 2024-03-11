
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-11 19:00:00 EET+0200 2024-03-11 20:00:00 EET+0200              12.452
	          2 2024-03-12 08:00:00 EET+0200 2024-03-12 10:00:00 EET+0200              12.099
	          3 2024-03-12 08:00:00 EET+0200 2024-03-12 11:00:00 EET+0200           11.823667
	          4 2024-03-12 08:00:00 EET+0200 2024-03-12 12:00:00 EET+0200            11.44425

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-12 00:00:00 EET+0200 2024-03-12 01:00:00 EET+0200               7.434
	          2 2024-03-11 23:00:00 EET+0200 2024-03-12 01:00:00 EET+0200               7.651
	          3 2024-03-11 23:00:00 EET+0200 2024-03-12 02:00:00 EET+0200               7.769
	          4 2024-03-12 00:00:00 EET+0200 2024-03-12 04:00:00 EET+0200             7.78925


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
