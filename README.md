
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-27 09:00:00 EET+0200 2024-03-27 10:00:00 EET+0200               7.405
	          2 2024-03-27 09:00:00 EET+0200 2024-03-27 11:00:00 EET+0200              7.0945
	          3 2024-03-27 08:00:00 EET+0200 2024-03-27 11:00:00 EET+0200               6.944
	          4 2024-03-27 08:00:00 EET+0200 2024-03-27 12:00:00 EET+0200               6.744

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-28 00:00:00 EET+0200 2024-03-28 01:00:00 EET+0200               5.215
	          2 2024-03-27 23:00:00 EET+0200 2024-03-28 01:00:00 EET+0200              5.2735
	          3 2024-03-27 22:00:00 EET+0200 2024-03-28 01:00:00 EET+0200            5.318667
	          4 2024-03-27 21:00:00 EET+0200 2024-03-28 01:00:00 EET+0200              5.3775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
