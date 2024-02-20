
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-20 18:00:00 EET+0200 2024-02-20 19:00:00 EET+0200              11.541
	          2 2024-02-20 18:00:00 EET+0200 2024-02-20 20:00:00 EET+0200              11.491
	          3 2024-02-20 17:00:00 EET+0200 2024-02-20 20:00:00 EET+0200           11.425667
	          4 2024-02-20 16:00:00 EET+0200 2024-02-20 20:00:00 EET+0200             10.8955

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-22 00:00:00 EET+0200 2024-02-22 01:00:00 EET+0200               4.263
	          2 2024-02-21 00:00:00 EET+0200 2024-02-21 02:00:00 EET+0200              4.5495
	          3 2024-02-21 00:00:00 EET+0200 2024-02-21 03:00:00 EET+0200            4.553667
	          4 2024-02-21 00:00:00 EET+0200 2024-02-21 04:00:00 EET+0200             4.55675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
