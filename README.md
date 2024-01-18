
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-19 18:00:00 EET+0200 2024-01-19 19:00:00 EET+0200              14.231
	          2 2024-01-19 18:00:00 EET+0200 2024-01-19 20:00:00 EET+0200              13.842
	          3 2024-01-19 18:00:00 EET+0200 2024-01-19 21:00:00 EET+0200           13.611333
	          4 2024-01-19 17:00:00 EET+0200 2024-01-19 21:00:00 EET+0200              13.451

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-19 04:00:00 EET+0200 2024-01-19 05:00:00 EET+0200               7.782
	          2 2024-01-19 04:00:00 EET+0200 2024-01-19 06:00:00 EET+0200               7.817
	          3 2024-01-19 03:00:00 EET+0200 2024-01-19 06:00:00 EET+0200            7.858667
	          4 2024-01-19 02:00:00 EET+0200 2024-01-19 06:00:00 EET+0200              7.9195


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
