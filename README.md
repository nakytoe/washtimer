
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-27 17:00:00 EET+0200 2023-12-27 18:00:00 EET+0200              10.453
	          2 2023-12-27 17:00:00 EET+0200 2023-12-27 19:00:00 EET+0200             10.4145
	          3 2023-12-27 17:00:00 EET+0200 2023-12-27 20:00:00 EET+0200              10.253
	          4 2023-12-27 16:00:00 EET+0200 2023-12-27 20:00:00 EET+0200            10.15025

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-28 04:00:00 EET+0200 2023-12-28 05:00:00 EET+0200               3.143
	          2 2023-12-28 03:00:00 EET+0200 2023-12-28 05:00:00 EET+0200              3.2915
	          3 2023-12-28 02:00:00 EET+0200 2023-12-28 05:00:00 EET+0200            3.427333
	          4 2023-12-28 02:00:00 EET+0200 2023-12-28 06:00:00 EET+0200              3.5005


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
