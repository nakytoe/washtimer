
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-07 08:00:00 EET+0200 2024-03-07 09:00:00 EET+0200              24.799
	          2 2024-03-07 08:00:00 EET+0200 2024-03-07 10:00:00 EET+0200              21.265
	          3 2024-03-07 07:00:00 EET+0200 2024-03-07 10:00:00 EET+0200           19.551333
	          4 2024-03-07 06:00:00 EET+0200 2024-03-07 10:00:00 EET+0200              17.238

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-07 15:00:00 EET+0200 2024-03-07 16:00:00 EET+0200               8.353
	          2 2024-03-07 04:00:00 EET+0200 2024-03-07 06:00:00 EET+0200               8.593
	          3 2024-03-07 03:00:00 EET+0200 2024-03-07 06:00:00 EET+0200               8.636
	          4 2024-03-07 02:00:00 EET+0200 2024-03-07 06:00:00 EET+0200               8.719


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
