
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-13 18:00:00 EET+0200 2024-03-13 19:00:00 EET+0200               13.81
	          2 2024-03-13 17:00:00 EET+0200 2024-03-13 19:00:00 EET+0200             11.2495
	          3 2024-03-13 17:00:00 EET+0200 2024-03-13 20:00:00 EET+0200              10.396
	          4 2024-03-13 15:00:00 EET+0200 2024-03-13 19:00:00 EET+0200            10.66225

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-15 00:00:00 EET+0200 2024-03-15 01:00:00 EET+0200              -0.009
	          2 2024-03-14 23:00:00 EET+0200 2024-03-15 01:00:00 EET+0200              0.0015
	          3 2024-03-14 22:00:00 EET+0200 2024-03-15 01:00:00 EET+0200            0.145333
	          4 2024-03-14 21:00:00 EET+0200 2024-03-15 01:00:00 EET+0200               0.551


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
