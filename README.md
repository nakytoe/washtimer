
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-30 19:00:00 EET+0200 2024-03-30 20:00:00 EET+0200               7.129
	          2 2024-03-30 18:00:00 EET+0200 2024-03-30 20:00:00 EET+0200              7.0775
	          3 2024-03-30 18:00:00 EET+0200 2024-03-30 21:00:00 EET+0200            6.980667
	          4 2024-03-30 18:00:00 EET+0200 2024-03-30 22:00:00 EET+0200              6.8415

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-30 14:00:00 EET+0200 2024-03-30 15:00:00 EET+0200               1.581
	          2 2024-03-30 14:00:00 EET+0200 2024-03-30 16:00:00 EET+0200              1.7985
	          3 2024-03-30 13:00:00 EET+0200 2024-03-30 16:00:00 EET+0200               2.263
	          4 2024-03-30 12:00:00 EET+0200 2024-03-30 16:00:00 EET+0200             2.47475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
