
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-03 15:00:00 EET+0200 2023-11-03 16:00:00 EET+0200               2.279
	          2 2023-11-03 15:00:00 EET+0200 2023-11-03 17:00:00 EET+0200              2.2435
	          3 2023-11-03 15:00:00 EET+0200 2023-11-03 18:00:00 EET+0200            2.216667
	          4 2023-11-03 15:00:00 EET+0200 2023-11-03 19:00:00 EET+0200              2.2015

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-05 00:00:00 EET+0200 2023-11-05 01:00:00 EET+0200               0.022
	          2 2023-11-04 23:00:00 EET+0200 2023-11-05 01:00:00 EET+0200              0.1925
	          3 2023-11-04 22:00:00 EET+0200 2023-11-05 01:00:00 EET+0200            0.290667
	          4 2023-11-04 21:00:00 EET+0200 2023-11-05 01:00:00 EET+0200             0.24525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
