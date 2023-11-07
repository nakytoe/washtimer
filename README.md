
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-07 19:00:00 EET+0200 2023-11-07 20:00:00 EET+0200              17.948
	          2 2023-11-07 18:00:00 EET+0200 2023-11-07 20:00:00 EET+0200              17.212
	          3 2023-11-07 17:00:00 EET+0200 2023-11-07 20:00:00 EET+0200           16.005667
	          4 2023-11-07 16:00:00 EET+0200 2023-11-07 20:00:00 EET+0200              15.096

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-09 00:00:00 EET+0200 2023-11-09 01:00:00 EET+0200               3.804
	          2 2023-11-08 23:00:00 EET+0200 2023-11-09 01:00:00 EET+0200               4.376
	          3 2023-11-08 03:00:00 EET+0200 2023-11-08 06:00:00 EET+0200            4.475667
	          4 2023-11-08 02:00:00 EET+0200 2023-11-08 06:00:00 EET+0200              4.5155


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
