
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-06 19:00:00 EET+0200 2023-11-06 20:00:00 EET+0200              18.136
	          2 2023-11-06 18:00:00 EET+0200 2023-11-06 20:00:00 EET+0200              17.356
	          3 2023-11-06 17:00:00 EET+0200 2023-11-06 20:00:00 EET+0200           16.072667
	          4 2023-11-06 17:00:00 EET+0200 2023-11-06 21:00:00 EET+0200             15.0145

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-06 04:00:00 EET+0200 2023-11-06 05:00:00 EET+0200               2.068
	          2 2023-11-06 03:00:00 EET+0200 2023-11-06 05:00:00 EET+0200              2.0825
	          3 2023-11-06 03:00:00 EET+0200 2023-11-06 06:00:00 EET+0200            2.088667
	          4 2023-11-06 02:00:00 EET+0200 2023-11-06 06:00:00 EET+0200               2.093


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
