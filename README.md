
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-21 16:00:00 EET+0200 2024-01-21 17:00:00 EET+0200               4.654
	          2 2024-01-21 16:00:00 EET+0200 2024-01-21 18:00:00 EET+0200              4.6465
	          3 2024-01-21 15:00:00 EET+0200 2024-01-21 18:00:00 EET+0200            4.628667
	          4 2024-01-21 15:00:00 EET+0200 2024-01-21 19:00:00 EET+0200               4.585

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-22 04:00:00 EET+0200 2024-01-22 05:00:00 EET+0200               0.625
	          2 2024-01-22 04:00:00 EET+0200 2024-01-22 06:00:00 EET+0200               0.626
	          3 2024-01-22 03:00:00 EET+0200 2024-01-22 06:00:00 EET+0200               1.187
	          4 2024-01-22 03:00:00 EET+0200 2024-01-22 07:00:00 EET+0200             1.51025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
