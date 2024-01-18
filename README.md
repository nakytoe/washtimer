
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-18 11:00:00 EET+0200 2024-01-18 12:00:00 EET+0200              13.752
	          2 2024-01-18 11:00:00 EET+0200 2024-01-18 13:00:00 EET+0200              13.569
	          3 2024-01-18 09:00:00 EET+0200 2024-01-18 12:00:00 EET+0200              13.149
	          4 2024-01-18 09:00:00 EET+0200 2024-01-18 13:00:00 EET+0200            13.20825

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-18 06:00:00 EET+0200 2024-01-18 07:00:00 EET+0200               7.555
	          2 2024-01-18 06:00:00 EET+0200 2024-01-18 08:00:00 EET+0200              8.5015
	          3 2024-01-18 22:00:00 EET+0200 2024-01-19 01:00:00 EET+0200               9.502
	          4 2024-01-18 21:00:00 EET+0200 2024-01-19 01:00:00 EET+0200              9.8225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
