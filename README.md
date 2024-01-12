
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-12 17:00:00 EET+0200 2024-01-12 18:00:00 EET+0200              37.078
	          2 2024-01-12 16:00:00 EET+0200 2024-01-12 18:00:00 EET+0200              31.125
	          3 2024-01-12 16:00:00 EET+0200 2024-01-12 19:00:00 EET+0200              29.017
	          4 2024-01-12 16:00:00 EET+0200 2024-01-12 20:00:00 EET+0200            26.56775

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-13 04:00:00 EET+0200 2024-01-13 05:00:00 EET+0200               5.266
	          2 2024-01-13 04:00:00 EET+0200 2024-01-13 06:00:00 EET+0200              5.2705
	          3 2024-01-13 04:00:00 EET+0200 2024-01-13 07:00:00 EET+0200               5.313
	          4 2024-01-13 03:00:00 EET+0200 2024-01-13 07:00:00 EET+0200             5.34875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
