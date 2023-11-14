
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-14 17:00:00 EET+0200 2023-11-14 18:00:00 EET+0200              16.742
	          2 2023-11-14 16:00:00 EET+0200 2023-11-14 18:00:00 EET+0200             16.0625
	          3 2023-11-14 16:00:00 EET+0200 2023-11-14 19:00:00 EET+0200              15.835
	          4 2023-11-14 16:00:00 EET+0200 2023-11-14 20:00:00 EET+0200            15.72075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-15 00:00:00 EET+0200 2023-11-15 01:00:00 EET+0200               7.689
	          2 2023-11-15 00:00:00 EET+0200 2023-11-15 02:00:00 EET+0200              8.8725
	          3 2023-11-15 03:00:00 EET+0200 2023-11-15 06:00:00 EET+0200            9.012667
	          4 2023-11-15 00:00:00 EET+0200 2023-11-15 04:00:00 EET+0200             9.06525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
