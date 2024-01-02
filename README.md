
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-02 16:00:00 EET+0200 2024-01-02 17:00:00 EET+0200              31.002
	          2 2024-01-02 16:00:00 EET+0200 2024-01-02 18:00:00 EET+0200              29.526
	          3 2024-01-02 16:00:00 EET+0200 2024-01-02 19:00:00 EET+0200           27.822667
	          4 2024-01-02 16:00:00 EET+0200 2024-01-02 20:00:00 EET+0200            28.61725

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-03 01:00:00 EET+0200 2024-01-03 02:00:00 EET+0200               6.086
	          2 2024-01-03 01:00:00 EET+0200 2024-01-03 03:00:00 EET+0200               6.562
	          3 2024-01-03 01:00:00 EET+0200 2024-01-03 04:00:00 EET+0200               6.694
	          4 2024-01-03 01:00:00 EET+0200 2024-01-03 05:00:00 EET+0200             6.81725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
