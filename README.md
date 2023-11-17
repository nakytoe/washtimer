
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-17 18:00:00 EET+0200 2023-11-17 19:00:00 EET+0200              18.144
	          2 2023-11-17 18:00:00 EET+0200 2023-11-17 20:00:00 EET+0200              18.078
	          3 2023-11-17 17:00:00 EET+0200 2023-11-17 20:00:00 EET+0200           17.716333
	          4 2023-11-17 17:00:00 EET+0200 2023-11-17 21:00:00 EET+0200             17.5315

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-18 00:00:00 EET+0200 2023-11-18 01:00:00 EET+0200              11.492
	          2 2023-11-17 23:00:00 EET+0200 2023-11-18 01:00:00 EET+0200              11.729
	          3 2023-11-17 22:00:00 EET+0200 2023-11-18 01:00:00 EET+0200              12.386
	          4 2023-11-17 21:00:00 EET+0200 2023-11-18 01:00:00 EET+0200            13.13775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
