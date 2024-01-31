
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-31 15:00:00 EET+0200 2024-01-31 16:00:00 EET+0200               2.108
	          2 2024-01-31 17:00:00 EET+0200 2024-01-31 19:00:00 EET+0200              2.0845
	          3 2024-01-31 15:00:00 EET+0200 2024-01-31 18:00:00 EET+0200            2.077333
	          4 2024-01-31 15:00:00 EET+0200 2024-01-31 19:00:00 EET+0200             2.07475

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-01 04:00:00 EET+0200 2024-02-01 05:00:00 EET+0200               -0.25
	          2 2024-02-01 03:00:00 EET+0200 2024-02-01 05:00:00 EET+0200             -0.2495
	          3 2024-02-01 02:00:00 EET+0200 2024-02-01 05:00:00 EET+0200           -0.240333
	          4 2024-02-01 01:00:00 EET+0200 2024-02-01 05:00:00 EET+0200              -0.232


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
