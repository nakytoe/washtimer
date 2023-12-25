
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-26 19:00:00 EET+0200 2023-12-26 20:00:00 EET+0200               6.566
	          2 2023-12-26 18:00:00 EET+0200 2023-12-26 20:00:00 EET+0200              6.5615
	          3 2023-12-26 18:00:00 EET+0200 2023-12-26 21:00:00 EET+0200               6.417
	          4 2023-12-26 17:00:00 EET+0200 2023-12-26 21:00:00 EET+0200               6.284

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-26 03:00:00 EET+0200 2023-12-26 04:00:00 EET+0200               3.384
	          2 2023-12-26 02:00:00 EET+0200 2023-12-26 04:00:00 EET+0200              3.4325
	          3 2023-12-26 02:00:00 EET+0200 2023-12-26 05:00:00 EET+0200               3.465
	          4 2023-12-26 01:00:00 EET+0200 2023-12-26 05:00:00 EET+0200             3.54825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
