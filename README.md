
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-31 08:00:00 EET+0200 2024-01-31 09:00:00 EET+0200               6.542
	          2 2024-01-31 08:00:00 EET+0200 2024-01-31 10:00:00 EET+0200               5.751
	          3 2024-01-31 08:00:00 EET+0200 2024-01-31 11:00:00 EET+0200            4.752333
	          4 2024-01-31 07:00:00 EET+0200 2024-01-31 11:00:00 EET+0200              4.2425

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-01 00:00:00 EET+0200 2024-02-01 01:00:00 EET+0200              -0.202
	          2 2024-01-31 23:00:00 EET+0200 2024-02-01 01:00:00 EET+0200             -0.1455
	          3 2024-01-31 22:00:00 EET+0200 2024-02-01 01:00:00 EET+0200           -0.099333
	          4 2024-01-31 21:00:00 EET+0200 2024-02-01 01:00:00 EET+0200             -0.0745


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
