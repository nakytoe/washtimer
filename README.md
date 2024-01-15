
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-15 13:00:00 EET+0200 2024-01-15 14:00:00 EET+0200              16.006
	          2 2024-01-15 13:00:00 EET+0200 2024-01-15 15:00:00 EET+0200              16.006
	          3 2024-01-15 12:00:00 EET+0200 2024-01-15 15:00:00 EET+0200           16.003333
	          4 2024-01-15 12:00:00 EET+0200 2024-01-15 16:00:00 EET+0200            15.83975

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-15 06:00:00 EET+0200 2024-01-15 07:00:00 EET+0200               8.751
	          2 2024-01-15 06:00:00 EET+0200 2024-01-15 08:00:00 EET+0200              9.6945
	          3 2024-01-15 22:00:00 EET+0200 2024-01-16 01:00:00 EET+0200           11.113333
	          4 2024-01-15 21:00:00 EET+0200 2024-01-16 01:00:00 EET+0200            11.53275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
