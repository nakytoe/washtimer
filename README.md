
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-15 14:00:00 EET+0200 2023-11-15 15:00:00 EET+0200               16.74
	          2 2023-11-15 18:00:00 EET+0200 2023-11-15 20:00:00 EET+0200               15.98
	          3 2023-11-15 17:00:00 EET+0200 2023-11-15 20:00:00 EET+0200           15.735667
	          4 2023-11-15 16:00:00 EET+0200 2023-11-15 20:00:00 EET+0200            15.55925

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-15 06:00:00 EET+0200 2023-11-15 07:00:00 EET+0200              10.004
	          2 2023-11-15 23:00:00 EET+0200 2023-11-16 01:00:00 EET+0200              10.904
	          3 2023-11-15 22:00:00 EET+0200 2023-11-16 01:00:00 EET+0200           11.299333
	          4 2023-11-15 21:00:00 EET+0200 2023-11-16 01:00:00 EET+0200             11.8815


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
