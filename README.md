
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-10-29 18:00:00 EET+0200 2023-10-29 19:00:00 EET+0200               8.163
	          2 2023-10-29 17:00:00 EET+0200 2023-10-29 19:00:00 EET+0200              7.8425
	          3 2023-10-29 17:00:00 EET+0200 2023-10-29 20:00:00 EET+0200            7.654333
	          4 2023-10-29 17:00:00 EET+0200 2023-10-29 21:00:00 EET+0200             7.10825

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-10-29 14:00:00 EET+0200 2023-10-29 15:00:00 EET+0200                2.78
	          2 2023-10-29 14:00:00 EET+0200 2023-10-29 16:00:00 EET+0200               2.814
	          3 2023-10-29 13:00:00 EET+0200 2023-10-29 16:00:00 EET+0200            2.830333
	          4 2023-10-29 12:00:00 EET+0200 2023-10-29 16:00:00 EET+0200              2.8575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
