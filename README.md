
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-07 08:00:00 EET+0200 2023-12-07 09:00:00 EET+0200              15.799
	          2 2023-12-07 13:00:00 EET+0200 2023-12-07 15:00:00 EET+0200              14.756
	          3 2023-12-07 13:00:00 EET+0200 2023-12-07 16:00:00 EET+0200           14.109667
	          4 2023-12-07 13:00:00 EET+0200 2023-12-07 17:00:00 EET+0200            13.85275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-08 00:00:00 EET+0200 2023-12-08 01:00:00 EET+0200              10.798
	          2 2023-12-07 23:00:00 EET+0200 2023-12-08 01:00:00 EET+0200             11.2035
	          3 2023-12-07 22:00:00 EET+0200 2023-12-08 01:00:00 EET+0200           11.362333
	          4 2023-12-07 21:00:00 EET+0200 2023-12-08 01:00:00 EET+0200             11.4895


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
