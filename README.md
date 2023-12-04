
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-04 17:00:00 EET+0200 2023-12-04 18:00:00 EET+0200              32.579
	          2 2023-12-04 16:00:00 EET+0200 2023-12-04 18:00:00 EET+0200             29.2945
	          3 2023-12-04 16:00:00 EET+0200 2023-12-04 19:00:00 EET+0200           28.058667
	          4 2023-12-04 08:00:00 EET+0200 2023-12-04 12:00:00 EET+0200             27.2015

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-05 00:00:00 EET+0200 2023-12-05 01:00:00 EET+0200              11.754
	          2 2023-12-04 23:00:00 EET+0200 2023-12-05 01:00:00 EET+0200              12.891
	          3 2023-12-04 22:00:00 EET+0200 2023-12-05 01:00:00 EET+0200               13.64
	          4 2023-12-04 21:00:00 EET+0200 2023-12-05 01:00:00 EET+0200             14.1795


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
