
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-23 18:00:00 EET+0200 2024-01-23 19:00:00 EET+0200               8.489
	          2 2024-01-23 18:00:00 EET+0200 2024-01-23 20:00:00 EET+0200               8.385
	          3 2024-01-23 17:00:00 EET+0200 2024-01-23 20:00:00 EET+0200            8.274667
	          4 2024-01-23 17:00:00 EET+0200 2024-01-23 21:00:00 EET+0200              8.1695

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-23 06:00:00 EET+0200 2024-01-23 07:00:00 EET+0200               2.682
	          2 2024-01-23 06:00:00 EET+0200 2024-01-23 08:00:00 EET+0200              2.9365
	          3 2024-01-23 06:00:00 EET+0200 2024-01-23 09:00:00 EET+0200            3.172333
	          4 2024-01-23 12:00:00 EET+0200 2024-01-23 16:00:00 EET+0200                3.34


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
