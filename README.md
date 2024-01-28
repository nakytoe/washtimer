
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-29 10:00:00 EET+0200 2024-01-29 11:00:00 EET+0200               2.697
	          2 2024-01-29 10:00:00 EET+0200 2024-01-29 12:00:00 EET+0200              2.6715
	          3 2024-01-29 10:00:00 EET+0200 2024-01-29 13:00:00 EET+0200            2.652333
	          4 2024-01-29 09:00:00 EET+0200 2024-01-29 13:00:00 EET+0200              2.6265

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-29 03:00:00 EET+0200 2024-01-29 04:00:00 EET+0200              -0.178
	          2 2024-01-29 03:00:00 EET+0200 2024-01-29 05:00:00 EET+0200             -0.1775
	          3 2024-01-29 02:00:00 EET+0200 2024-01-29 05:00:00 EET+0200           -0.175667
	          4 2024-01-29 02:00:00 EET+0200 2024-01-29 06:00:00 EET+0200              -0.167


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
