
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-08 19:00:00 EET+0200 2024-03-08 20:00:00 EET+0200              14.863
	          2 2024-03-08 18:00:00 EET+0200 2024-03-08 20:00:00 EET+0200             14.6385
	          3 2024-03-08 18:00:00 EET+0200 2024-03-08 21:00:00 EET+0200              14.276
	          4 2024-03-08 17:00:00 EET+0200 2024-03-08 21:00:00 EET+0200              13.187

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-08 04:00:00 EET+0200 2024-03-08 05:00:00 EET+0200               7.937
	          2 2024-03-08 03:00:00 EET+0200 2024-03-08 05:00:00 EET+0200              7.9905
	          3 2024-03-08 02:00:00 EET+0200 2024-03-08 05:00:00 EET+0200               8.009
	          4 2024-03-08 01:00:00 EET+0200 2024-03-08 05:00:00 EET+0200             8.07775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
