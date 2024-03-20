
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-20 08:00:00 EET+0200 2024-03-20 09:00:00 EET+0200              13.882
	          2 2024-03-20 08:00:00 EET+0200 2024-03-20 10:00:00 EET+0200              12.891
	          3 2024-03-20 08:00:00 EET+0200 2024-03-20 11:00:00 EET+0200           11.442667
	          4 2024-03-20 08:00:00 EET+0200 2024-03-20 12:00:00 EET+0200             10.6035

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-20 06:00:00 EET+0200 2024-03-20 07:00:00 EET+0200               6.222
	          2 2024-03-20 06:00:00 EET+0200 2024-03-20 08:00:00 EET+0200              6.8145
	          3 2024-03-20 22:00:00 EET+0200 2024-03-21 01:00:00 EET+0200            7.381667
	          4 2024-03-20 21:00:00 EET+0200 2024-03-21 01:00:00 EET+0200             7.55175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
