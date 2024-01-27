
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-27 11:00:00 EET+0200 2024-01-27 12:00:00 EET+0200                2.62
	          2 2024-01-27 10:00:00 EET+0200 2024-01-27 12:00:00 EET+0200               2.614
	          3 2024-01-27 10:00:00 EET+0200 2024-01-27 13:00:00 EET+0200            2.611333
	          4 2024-01-27 09:00:00 EET+0200 2024-01-27 13:00:00 EET+0200              2.6095

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-28 00:00:00 EET+0200 2024-01-28 01:00:00 EET+0200               0.342
	          2 2024-01-27 23:00:00 EET+0200 2024-01-28 01:00:00 EET+0200               0.387
	          3 2024-01-27 22:00:00 EET+0200 2024-01-28 01:00:00 EET+0200               0.677
	          4 2024-01-27 21:00:00 EET+0200 2024-01-28 01:00:00 EET+0200             0.97675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
