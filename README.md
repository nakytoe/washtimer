
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-14 19:00:00 EET+0200 2024-01-14 20:00:00 EET+0200              11.735
	          2 2024-01-14 18:00:00 EET+0200 2024-01-14 20:00:00 EET+0200              11.563
	          3 2024-01-14 17:00:00 EET+0200 2024-01-14 20:00:00 EET+0200              11.289
	          4 2024-01-14 17:00:00 EET+0200 2024-01-14 21:00:00 EET+0200            11.10975

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-13 15:00:00 EET+0200 2024-01-13 16:00:00 EET+0200               7.337
	          2 2024-01-14 02:00:00 EET+0200 2024-01-14 04:00:00 EET+0200              7.7525
	          3 2024-01-14 00:00:00 EET+0200 2024-01-14 03:00:00 EET+0200            7.761667
	          4 2024-01-14 00:00:00 EET+0200 2024-01-14 04:00:00 EET+0200               7.772


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
