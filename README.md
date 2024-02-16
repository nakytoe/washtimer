
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-16 18:00:00 EET+0200 2024-02-16 19:00:00 EET+0200               4.319
	          2 2024-02-16 17:00:00 EET+0200 2024-02-16 19:00:00 EET+0200              4.2645
	          3 2024-02-16 16:00:00 EET+0200 2024-02-16 19:00:00 EET+0200            4.136333
	          4 2024-02-16 15:00:00 EET+0200 2024-02-16 19:00:00 EET+0200               4.105

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-17 06:00:00 EET+0200 2024-02-17 07:00:00 EET+0200               1.239
	          2 2024-02-17 06:00:00 EET+0200 2024-02-17 08:00:00 EET+0200              1.3085
	          3 2024-02-17 05:00:00 EET+0200 2024-02-17 08:00:00 EET+0200            1.333667
	          4 2024-02-17 04:00:00 EET+0200 2024-02-17 08:00:00 EET+0200                1.41


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
