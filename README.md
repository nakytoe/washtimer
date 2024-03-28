
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-28 18:00:00 EET+0200 2024-03-28 19:00:00 EET+0200               5.497
	          2 2024-03-28 18:00:00 EET+0200 2024-03-28 20:00:00 EET+0200              5.4575
	          3 2024-03-28 18:00:00 EET+0200 2024-03-28 21:00:00 EET+0200            5.395667
	          4 2024-03-28 18:00:00 EET+0200 2024-03-28 22:00:00 EET+0200             5.25325

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-29 14:00:00 EET+0200 2024-03-29 15:00:00 EET+0200               1.223
	          2 2024-03-29 04:00:00 EET+0200 2024-03-29 06:00:00 EET+0200               1.364
	          3 2024-03-29 03:00:00 EET+0200 2024-03-29 06:00:00 EET+0200            1.410667
	          4 2024-03-29 03:00:00 EET+0200 2024-03-29 07:00:00 EET+0200             1.45375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
