
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-24 20:00:00 EET+0200 2024-02-24 21:00:00 EET+0200               5.326
	          2 2024-02-24 19:00:00 EET+0200 2024-02-24 21:00:00 EET+0200               5.141
	          3 2024-02-24 20:00:00 EET+0200 2024-02-24 23:00:00 EET+0200            5.101333
	          4 2024-02-24 20:00:00 EET+0200 2024-02-25 00:00:00 EET+0200             5.08275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-25 16:00:00 EET+0200 2024-02-25 17:00:00 EET+0200               3.719
	          2 2024-02-25 15:00:00 EET+0200 2024-02-25 17:00:00 EET+0200              3.7205
	          3 2024-02-25 14:00:00 EET+0200 2024-02-25 17:00:00 EET+0200               3.725
	          4 2024-02-25 13:00:00 EET+0200 2024-02-25 17:00:00 EET+0200              3.7365


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
