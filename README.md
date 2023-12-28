
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-28 16:00:00 EET+0200 2023-12-28 17:00:00 EET+0200               8.707
	          2 2023-12-28 16:00:00 EET+0200 2023-12-28 18:00:00 EET+0200               8.691
	          3 2023-12-28 16:00:00 EET+0200 2023-12-28 19:00:00 EET+0200            8.639333
	          4 2023-12-28 16:00:00 EET+0200 2023-12-28 20:00:00 EET+0200               8.426

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-29 04:00:00 EET+0200 2023-12-29 05:00:00 EET+0200               2.337
	          2 2023-12-29 03:00:00 EET+0200 2023-12-29 05:00:00 EET+0200               2.409
	          3 2023-12-29 03:00:00 EET+0200 2023-12-29 06:00:00 EET+0200               2.439
	          4 2023-12-29 02:00:00 EET+0200 2023-12-29 06:00:00 EET+0200               2.475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
