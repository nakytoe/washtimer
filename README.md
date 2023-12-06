
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-06 18:00:00 EET+0200 2023-12-06 19:00:00 EET+0200              22.081
	          2 2023-12-06 09:00:00 EET+0200 2023-12-06 11:00:00 EET+0200             21.2975
	          3 2023-12-06 17:00:00 EET+0200 2023-12-06 20:00:00 EET+0200           20.970667
	          4 2023-12-06 17:00:00 EET+0200 2023-12-06 21:00:00 EET+0200            20.37575

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-07 00:00:00 EET+0200 2023-12-07 01:00:00 EET+0200               12.12
	          2 2023-12-06 23:00:00 EET+0200 2023-12-07 01:00:00 EET+0200              12.508
	          3 2023-12-06 22:00:00 EET+0200 2023-12-07 01:00:00 EET+0200           12.981667
	          4 2023-12-06 21:00:00 EET+0200 2023-12-07 01:00:00 EET+0200             13.6465


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
