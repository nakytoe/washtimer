
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-15 16:00:00 EET+0200 2023-12-15 17:00:00 EET+0200              24.801
	          2 2023-12-15 15:00:00 EET+0200 2023-12-15 17:00:00 EET+0200              22.982
	          3 2023-12-15 16:00:00 EET+0200 2023-12-15 19:00:00 EET+0200           22.470333
	          4 2023-12-15 15:00:00 EET+0200 2023-12-15 19:00:00 EET+0200             22.1435

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-17 00:00:00 EET+0200 2023-12-17 01:00:00 EET+0200               0.001
	          2 2023-12-16 23:00:00 EET+0200 2023-12-17 01:00:00 EET+0200              0.0025
	          3 2023-12-16 22:00:00 EET+0200 2023-12-17 01:00:00 EET+0200            0.093333
	          4 2023-12-16 21:00:00 EET+0200 2023-12-17 01:00:00 EET+0200              0.2235


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
