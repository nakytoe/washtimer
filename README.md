
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-23 12:00:00 EET+0200 2023-11-23 13:00:00 EET+0200              10.932
	          2 2023-11-23 12:00:00 EET+0200 2023-11-23 14:00:00 EET+0200              10.922
	          3 2023-11-23 11:00:00 EET+0200 2023-11-23 14:00:00 EET+0200           10.901333
	          4 2023-11-23 10:00:00 EET+0200 2023-11-23 14:00:00 EET+0200            10.89375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-23 01:00:00 EET+0200 2023-11-23 02:00:00 EET+0200               0.625
	          2 2023-11-23 01:00:00 EET+0200 2023-11-23 03:00:00 EET+0200              0.9075
	          3 2023-11-23 01:00:00 EET+0200 2023-11-23 04:00:00 EET+0200               1.019
	          4 2023-11-23 01:00:00 EET+0200 2023-11-23 05:00:00 EET+0200               1.076


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
