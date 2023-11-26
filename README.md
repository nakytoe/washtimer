
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-26 19:00:00 EET+0200 2023-11-26 20:00:00 EET+0200              18.559
	          2 2023-11-26 18:00:00 EET+0200 2023-11-26 20:00:00 EET+0200             18.1955
	          3 2023-11-26 17:00:00 EET+0200 2023-11-26 20:00:00 EET+0200              18.125
	          4 2023-11-26 16:00:00 EET+0200 2023-11-26 20:00:00 EET+0200            18.08575

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-26 07:00:00 EET+0200 2023-11-26 08:00:00 EET+0200              12.259
	          2 2023-11-26 07:00:00 EET+0200 2023-11-26 09:00:00 EET+0200              12.466
	          3 2023-11-26 06:00:00 EET+0200 2023-11-26 09:00:00 EET+0200           12.855333
	          4 2023-11-26 06:00:00 EET+0200 2023-11-26 10:00:00 EET+0200            14.05025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
