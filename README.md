
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-27 15:00:00 EET+0200 2023-11-27 16:00:00 EET+0200              15.573
	          2 2023-11-27 15:00:00 EET+0200 2023-11-27 17:00:00 EET+0200             15.0685
	          3 2023-11-27 15:00:00 EET+0200 2023-11-27 18:00:00 EET+0200           14.719667
	          4 2023-11-27 15:00:00 EET+0200 2023-11-27 19:00:00 EET+0200             14.8075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-28 03:00:00 EET+0200 2023-11-28 04:00:00 EET+0200               2.518
	          2 2023-11-28 03:00:00 EET+0200 2023-11-28 05:00:00 EET+0200               2.525
	          3 2023-11-28 02:00:00 EET+0200 2023-11-28 05:00:00 EET+0200               2.533
	          4 2023-11-28 02:00:00 EET+0200 2023-11-28 06:00:00 EET+0200              2.5375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
