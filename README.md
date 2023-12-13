
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-13 17:00:00 EET+0200 2023-12-13 18:00:00 EET+0200              18.705
	          2 2023-12-13 08:00:00 EET+0200 2023-12-13 10:00:00 EET+0200                18.6
	          3 2023-12-13 07:00:00 EET+0200 2023-12-13 10:00:00 EET+0200           18.599667
	          4 2023-12-13 07:00:00 EET+0200 2023-12-13 11:00:00 EET+0200             18.5995

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-14 00:00:00 EET+0200 2023-12-14 01:00:00 EET+0200              11.286
	          2 2023-12-13 23:00:00 EET+0200 2023-12-14 01:00:00 EET+0200              12.104
	          3 2023-12-13 22:00:00 EET+0200 2023-12-14 01:00:00 EET+0200           12.231667
	          4 2023-12-13 21:00:00 EET+0200 2023-12-14 01:00:00 EET+0200             12.6665


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
