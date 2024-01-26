
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-26 18:00:00 EET+0200 2024-01-26 19:00:00 EET+0200               7.114
	          2 2024-01-26 18:00:00 EET+0200 2024-01-26 20:00:00 EET+0200               6.917
	          3 2024-01-26 17:00:00 EET+0200 2024-01-26 20:00:00 EET+0200            6.739333
	          4 2024-01-26 16:00:00 EET+0200 2024-01-26 20:00:00 EET+0200             6.57075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-28 00:00:00 EET+0200 2024-01-28 01:00:00 EET+0200               0.342
	          2 2024-01-27 23:00:00 EET+0200 2024-01-28 01:00:00 EET+0200               0.387
	          3 2024-01-27 22:00:00 EET+0200 2024-01-28 01:00:00 EET+0200               0.677
	          4 2024-01-27 21:00:00 EET+0200 2024-01-28 01:00:00 EET+0200             0.97675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
