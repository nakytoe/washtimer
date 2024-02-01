
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-01 10:00:00 EET+0200 2024-02-01 11:00:00 EET+0200               0.549
	          2 2024-02-01 09:00:00 EET+0200 2024-02-01 11:00:00 EET+0200               0.487
	          3 2024-02-01 09:00:00 EET+0200 2024-02-01 12:00:00 EET+0200            0.466333
	          4 2024-02-01 08:00:00 EET+0200 2024-02-01 12:00:00 EET+0200             0.44525

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-01 06:00:00 EET+0200 2024-02-01 07:00:00 EET+0200              -0.184
	          2 2024-02-01 06:00:00 EET+0200 2024-02-01 08:00:00 EET+0200              -0.097
	          3 2024-02-01 22:00:00 EET+0200 2024-02-02 01:00:00 EET+0200           -0.000333
	          4 2024-02-01 21:00:00 EET+0200 2024-02-02 01:00:00 EET+0200            -0.00025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
