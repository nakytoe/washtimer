
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-20 17:00:00 EET+0200 2024-01-20 18:00:00 EET+0200              12.649
	          2 2024-01-20 17:00:00 EET+0200 2024-01-20 19:00:00 EET+0200             12.3635
	          3 2024-01-20 17:00:00 EET+0200 2024-01-20 20:00:00 EET+0200           12.421667
	          4 2024-01-20 16:00:00 EET+0200 2024-01-20 20:00:00 EET+0200             12.2885

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-22 00:00:00 EET+0200 2024-01-22 01:00:00 EET+0200                 3.6
	          2 2024-01-21 23:00:00 EET+0200 2024-01-22 01:00:00 EET+0200              3.9595
	          3 2024-01-21 22:00:00 EET+0200 2024-01-22 01:00:00 EET+0200            4.067667
	          4 2024-01-21 21:00:00 EET+0200 2024-01-22 01:00:00 EET+0200              4.1255


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
