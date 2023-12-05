
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-05 16:00:00 EET+0200 2023-12-05 17:00:00 EET+0200              28.141
	          2 2023-12-05 16:00:00 EET+0200 2023-12-05 18:00:00 EET+0200              28.066
	          3 2023-12-05 15:00:00 EET+0200 2023-12-05 18:00:00 EET+0200              26.944
	          4 2023-12-05 15:00:00 EET+0200 2023-12-05 19:00:00 EET+0200             25.5585

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-06 03:00:00 EET+0200 2023-12-06 04:00:00 EET+0200               12.05
	          2 2023-12-06 03:00:00 EET+0200 2023-12-06 05:00:00 EET+0200              12.194
	          3 2023-12-06 02:00:00 EET+0200 2023-12-06 05:00:00 EET+0200              12.755
	          4 2023-12-06 01:00:00 EET+0200 2023-12-06 05:00:00 EET+0200              12.749


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
