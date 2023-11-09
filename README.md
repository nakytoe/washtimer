
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-09 15:00:00 EET+0200 2023-11-09 16:00:00 EET+0200              12.179
	          2 2023-11-09 18:00:00 EET+0200 2023-11-09 20:00:00 EET+0200              11.645
	          3 2023-11-09 17:00:00 EET+0200 2023-11-09 20:00:00 EET+0200           11.566333
	          4 2023-11-09 17:00:00 EET+0200 2023-11-09 21:00:00 EET+0200            11.30325

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-11 00:00:00 EET+0200 2023-11-11 01:00:00 EET+0200               2.413
	          2 2023-11-10 23:00:00 EET+0200 2023-11-11 01:00:00 EET+0200              2.5715
	          3 2023-11-10 22:00:00 EET+0200 2023-11-11 01:00:00 EET+0200            2.653333
	          4 2023-11-10 21:00:00 EET+0200 2023-11-11 01:00:00 EET+0200               2.759


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
