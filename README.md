
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-18 17:00:00 EET+0200 2023-11-18 18:00:00 EET+0200              16.119
	          2 2023-11-18 17:00:00 EET+0200 2023-11-18 19:00:00 EET+0200              14.574
	          3 2023-11-18 17:00:00 EET+0200 2023-11-18 20:00:00 EET+0200           14.152667
	          4 2023-11-18 16:00:00 EET+0200 2023-11-18 20:00:00 EET+0200             13.8655

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-19 05:00:00 EET+0200 2023-11-19 06:00:00 EET+0200               4.349
	          2 2023-11-19 04:00:00 EET+0200 2023-11-19 06:00:00 EET+0200              4.4985
	          3 2023-11-19 04:00:00 EET+0200 2023-11-19 07:00:00 EET+0200               4.553
	          4 2023-11-19 04:00:00 EET+0200 2023-11-19 08:00:00 EET+0200                4.71


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
