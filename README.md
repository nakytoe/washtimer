
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-28 09:00:00 EET+0200 2024-02-28 10:00:00 EET+0200               3.415
	          2 2024-02-28 09:00:00 EET+0200 2024-02-28 11:00:00 EET+0200              3.4075
	          3 2024-02-28 09:00:00 EET+0200 2024-02-28 12:00:00 EET+0200                3.35
	          4 2024-02-28 08:00:00 EET+0200 2024-02-28 12:00:00 EET+0200              3.3085

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-29 00:00:00 EET+0200 2024-02-29 01:00:00 EET+0200               2.055
	          2 2024-02-28 23:00:00 EET+0200 2024-02-29 01:00:00 EET+0200               2.193
	          3 2024-02-28 22:00:00 EET+0200 2024-02-29 01:00:00 EET+0200               2.314
	          4 2024-02-28 21:00:00 EET+0200 2024-02-29 01:00:00 EET+0200             2.39775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
