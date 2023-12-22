
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-22 18:00:00 EET+0200 2023-12-22 19:00:00 EET+0200               5.171
	          2 2023-12-22 17:00:00 EET+0200 2023-12-22 19:00:00 EET+0200              5.1515
	          3 2023-12-22 17:00:00 EET+0200 2023-12-22 20:00:00 EET+0200            5.059667
	          4 2023-12-22 17:00:00 EET+0200 2023-12-22 21:00:00 EET+0200               4.916

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-23 00:00:00 EET+0200 2023-12-23 01:00:00 EET+0200               1.488
	          2 2023-12-22 23:00:00 EET+0200 2023-12-23 01:00:00 EET+0200              2.1435
	          3 2023-12-22 22:00:00 EET+0200 2023-12-23 01:00:00 EET+0200               2.459
	          4 2023-12-22 21:00:00 EET+0200 2023-12-23 01:00:00 EET+0200             2.60875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
