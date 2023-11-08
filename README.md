
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-08 09:00:00 EET+0200 2023-11-08 10:00:00 EET+0200              12.632
	          2 2023-11-08 09:00:00 EET+0200 2023-11-08 11:00:00 EET+0200             11.9415
	          3 2023-11-08 08:00:00 EET+0200 2023-11-08 11:00:00 EET+0200           11.512667
	          4 2023-11-08 08:00:00 EET+0200 2023-11-08 12:00:00 EET+0200            11.19925

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-09 00:00:00 EET+0200 2023-11-09 01:00:00 EET+0200               3.804
	          2 2023-11-08 23:00:00 EET+0200 2023-11-09 01:00:00 EET+0200               4.376
	          3 2023-11-08 22:00:00 EET+0200 2023-11-09 01:00:00 EET+0200            5.028333
	          4 2023-11-08 21:00:00 EET+0200 2023-11-09 01:00:00 EET+0200               5.608


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
