
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-07 16:00:00 EET+0200 2024-02-07 17:00:00 EET+0200              18.702
	          2 2024-02-07 16:00:00 EET+0200 2024-02-07 18:00:00 EET+0200              17.448
	          3 2024-02-07 16:00:00 EET+0200 2024-02-07 19:00:00 EET+0200           17.174667
	          4 2024-02-07 16:00:00 EET+0200 2024-02-07 20:00:00 EET+0200              17.171

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-08 04:00:00 EET+0200 2024-02-08 05:00:00 EET+0200               8.949
	          2 2024-02-08 03:00:00 EET+0200 2024-02-08 05:00:00 EET+0200               9.434
	          3 2024-02-08 02:00:00 EET+0200 2024-02-08 05:00:00 EET+0200            9.967333
	          4 2024-02-08 02:00:00 EET+0200 2024-02-08 06:00:00 EET+0200             10.2505


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
