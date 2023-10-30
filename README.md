
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-10-30 18:00:00 EET+0200 2023-10-30 19:00:00 EET+0200              16.118
	          2 2023-10-30 17:00:00 EET+0200 2023-10-30 19:00:00 EET+0200             16.1165
	          3 2023-10-30 16:00:00 EET+0200 2023-10-30 19:00:00 EET+0200           16.114333
	          4 2023-10-30 16:00:00 EET+0200 2023-10-30 20:00:00 EET+0200              16.113

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-10-31 00:00:00 EET+0200 2023-10-31 01:00:00 EET+0200               3.462
	          2 2023-10-30 23:00:00 EET+0200 2023-10-31 01:00:00 EET+0200               3.855
	          3 2023-10-30 22:00:00 EET+0200 2023-10-31 01:00:00 EET+0200            4.470667
	          4 2023-10-30 21:00:00 EET+0200 2023-10-31 01:00:00 EET+0200              5.2765


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
