
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-22 08:00:00 EET+0200 2024-01-22 09:00:00 EET+0200               4.117
	          2 2024-01-22 08:00:00 EET+0200 2024-01-22 10:00:00 EET+0200              4.1095
	          3 2024-01-22 08:00:00 EET+0200 2024-01-22 11:00:00 EET+0200            4.098333
	          4 2024-01-22 08:00:00 EET+0200 2024-01-22 12:00:00 EET+0200             4.05625

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-22 06:00:00 EET+0200 2024-01-22 07:00:00 EET+0200                2.48
	          2 2024-01-22 06:00:00 EET+0200 2024-01-22 08:00:00 EET+0200               2.855
	          3 2024-01-22 22:00:00 EET+0200 2024-01-23 01:00:00 EET+0200            3.221667
	          4 2024-01-22 21:00:00 EET+0200 2024-01-23 01:00:00 EET+0200                3.39


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
