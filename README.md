
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-13 22:00:00 EET+0200 2024-01-13 23:00:00 EET+0200               9.944
	          2 2024-01-13 21:00:00 EET+0200 2024-01-13 23:00:00 EET+0200              9.5015
	          3 2024-01-13 20:00:00 EET+0200 2024-01-13 23:00:00 EET+0200            9.385667
	          4 2024-01-13 19:00:00 EET+0200 2024-01-13 23:00:00 EET+0200             9.38925

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-13 06:00:00 EET+0200 2024-01-13 07:00:00 EET+0200               5.398
	          2 2024-01-13 06:00:00 EET+0200 2024-01-13 08:00:00 EET+0200              5.5275
	          3 2024-01-13 06:00:00 EET+0200 2024-01-13 09:00:00 EET+0200            5.801333
	          4 2024-01-13 06:00:00 EET+0200 2024-01-13 10:00:00 EET+0200             6.14675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
