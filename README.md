
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-26 19:00:00 EET+0200 2024-03-26 20:00:00 EET+0200              16.796
	          2 2024-03-26 18:00:00 EET+0200 2024-03-26 20:00:00 EET+0200               16.78
	          3 2024-03-26 17:00:00 EET+0200 2024-03-26 20:00:00 EET+0200              15.566
	          4 2024-03-26 16:00:00 EET+0200 2024-03-26 20:00:00 EET+0200            14.71275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-28 00:00:00 EET+0200 2024-03-28 01:00:00 EET+0200               5.215
	          2 2024-03-27 23:00:00 EET+0200 2024-03-28 01:00:00 EET+0200              5.2735
	          3 2024-03-27 22:00:00 EET+0200 2024-03-28 01:00:00 EET+0200            5.318667
	          4 2024-03-27 21:00:00 EET+0200 2024-03-28 01:00:00 EET+0200              5.3775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
