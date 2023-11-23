
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
	          1 2023-11-23 06:00:00 EET+0200 2023-11-23 07:00:00 EET+0200               2.036
	          2 2023-11-23 23:00:00 EET+0200 2023-11-24 01:00:00 EET+0200              3.1065
	          3 2023-11-23 22:00:00 EET+0200 2023-11-24 01:00:00 EET+0200               4.404
	          4 2023-11-23 21:00:00 EET+0200 2023-11-24 01:00:00 EET+0200             5.31775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
