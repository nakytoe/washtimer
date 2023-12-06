
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-06 18:00:00 EET+0200 2023-12-06 19:00:00 EET+0200              22.081
	          2 2023-12-06 18:00:00 EET+0200 2023-12-06 20:00:00 EET+0200              21.288
	          3 2023-12-06 17:00:00 EET+0200 2023-12-06 20:00:00 EET+0200           20.970667
	          4 2023-12-06 17:00:00 EET+0200 2023-12-06 21:00:00 EET+0200            20.37575

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-08 00:00:00 EET+0200 2023-12-08 01:00:00 EET+0200              10.798
	          2 2023-12-07 04:00:00 EET+0200 2023-12-07 06:00:00 EET+0200              11.133
	          3 2023-12-07 04:00:00 EET+0200 2023-12-07 07:00:00 EET+0200              11.282
	          4 2023-12-07 03:00:00 EET+0200 2023-12-07 07:00:00 EET+0200            11.37075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
