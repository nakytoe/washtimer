
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-22 20:00:00 EET+0200 2024-03-22 21:00:00 EET+0200               7.407
	          2 2024-03-22 19:00:00 EET+0200 2024-03-22 21:00:00 EET+0200               7.393
	          3 2024-03-22 18:00:00 EET+0200 2024-03-22 21:00:00 EET+0200            7.327333
	          4 2024-03-22 18:00:00 EET+0200 2024-03-22 22:00:00 EET+0200              7.1705

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-23 13:00:00 EET+0200 2024-03-23 14:00:00 EET+0200               1.283
	          2 2024-03-23 12:00:00 EET+0200 2024-03-23 14:00:00 EET+0200              1.2865
	          3 2024-03-23 11:00:00 EET+0200 2024-03-23 14:00:00 EET+0200               1.337
	          4 2024-03-23 11:00:00 EET+0200 2024-03-23 15:00:00 EET+0200             1.45275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
