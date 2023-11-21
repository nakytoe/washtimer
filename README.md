
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-21 16:00:00 EET+0200 2023-11-21 17:00:00 EET+0200               96.37
	          2 2023-11-21 15:00:00 EET+0200 2023-11-21 17:00:00 EET+0200             78.4375
	          3 2023-11-21 15:00:00 EET+0200 2023-11-21 18:00:00 EET+0200           66.572667
	          4 2023-11-21 13:00:00 EET+0200 2023-11-21 17:00:00 EET+0200            61.85075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-22 00:00:00 EET+0200 2023-11-22 01:00:00 EET+0200              12.157
	          2 2023-11-21 23:00:00 EET+0200 2023-11-22 01:00:00 EET+0200              12.955
	          3 2023-11-21 22:00:00 EET+0200 2023-11-22 01:00:00 EET+0200           15.045333
	          4 2023-11-21 21:00:00 EET+0200 2023-11-22 01:00:00 EET+0200            15.37875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
