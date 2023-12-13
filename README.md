
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-14 16:00:00 EET+0200 2023-12-14 17:00:00 EET+0200              23.358
	          2 2023-12-14 16:00:00 EET+0200 2023-12-14 18:00:00 EET+0200             23.3375
	          3 2023-12-14 16:00:00 EET+0200 2023-12-14 19:00:00 EET+0200           23.024333
	          4 2023-12-14 15:00:00 EET+0200 2023-12-14 19:00:00 EET+0200              22.073

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-14 02:00:00 EET+0200 2023-12-14 03:00:00 EET+0200               9.461
	          2 2023-12-14 02:00:00 EET+0200 2023-12-14 04:00:00 EET+0200               9.501
	          3 2023-12-14 01:00:00 EET+0200 2023-12-14 04:00:00 EET+0200            9.557667
	          4 2023-12-14 01:00:00 EET+0200 2023-12-14 05:00:00 EET+0200               9.586


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
