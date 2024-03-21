
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-21 19:00:00 EET+0200 2024-03-21 20:00:00 EET+0200              15.764
	          2 2024-03-21 19:00:00 EET+0200 2024-03-21 21:00:00 EET+0200              15.365
	          3 2024-03-21 18:00:00 EET+0200 2024-03-21 21:00:00 EET+0200              14.414
	          4 2024-03-21 18:00:00 EET+0200 2024-03-21 22:00:00 EET+0200            13.34975

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-22 04:00:00 EET+0200 2024-03-22 05:00:00 EET+0200               3.586
	          2 2024-03-22 04:00:00 EET+0200 2024-03-22 06:00:00 EET+0200               3.772
	          3 2024-03-22 03:00:00 EET+0200 2024-03-22 06:00:00 EET+0200            3.847333
	          4 2024-03-22 02:00:00 EET+0200 2024-03-22 06:00:00 EET+0200              3.9475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
