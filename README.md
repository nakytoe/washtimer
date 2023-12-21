
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-21 07:00:00 EET+0200 2023-12-21 08:00:00 EET+0200               8.519
	          2 2023-12-21 06:00:00 EET+0200 2023-12-21 08:00:00 EET+0200                7.67
	          3 2023-12-21 06:00:00 EET+0200 2023-12-21 09:00:00 EET+0200            7.386667
	          4 2023-12-21 06:00:00 EET+0200 2023-12-21 10:00:00 EET+0200               7.198

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-22 00:00:00 EET+0200 2023-12-22 01:00:00 EET+0200               2.258
	          2 2023-12-21 23:00:00 EET+0200 2023-12-22 01:00:00 EET+0200              2.9125
	          3 2023-12-21 22:00:00 EET+0200 2023-12-22 01:00:00 EET+0200               3.312
	          4 2023-12-21 21:00:00 EET+0200 2023-12-22 01:00:00 EET+0200               3.754


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
