
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-05 09:00:00 EET+0200 2023-12-05 10:00:00 EET+0200              41.168
	          2 2023-12-05 09:00:00 EET+0200 2023-12-05 11:00:00 EET+0200              36.089
	          3 2023-12-05 08:00:00 EET+0200 2023-12-05 11:00:00 EET+0200              34.395
	          4 2023-12-05 08:00:00 EET+0200 2023-12-05 12:00:00 EET+0200            33.54275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-05 00:00:00 EET+0200 2023-12-05 01:00:00 EET+0200              11.754
	          2 2023-12-05 00:00:00 EET+0200 2023-12-05 02:00:00 EET+0200             12.7025
	          3 2023-12-05 00:00:00 EET+0200 2023-12-05 03:00:00 EET+0200              13.018
	          4 2023-12-05 00:00:00 EET+0200 2023-12-05 04:00:00 EET+0200              13.175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
