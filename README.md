
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-07 10:00:00 EET+0200 2023-11-07 11:00:00 EET+0200              21.786
	          2 2023-11-07 09:00:00 EET+0200 2023-11-07 11:00:00 EET+0200             21.4385
	          3 2023-11-07 09:00:00 EET+0200 2023-11-07 12:00:00 EET+0200           21.321333
	          4 2023-11-07 08:00:00 EET+0200 2023-11-07 12:00:00 EET+0200             20.3255

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-08 00:00:00 EET+0200 2023-11-08 01:00:00 EET+0200               5.878
	          2 2023-11-07 23:00:00 EET+0200 2023-11-08 01:00:00 EET+0200              6.7955
	          3 2023-11-07 22:00:00 EET+0200 2023-11-08 01:00:00 EET+0200            7.872667
	          4 2023-11-07 21:00:00 EET+0200 2023-11-08 01:00:00 EET+0200               8.533


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
