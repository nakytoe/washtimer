
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-06 18:00:00 EET+0200 2024-02-06 19:00:00 EET+0200              30.991
	          2 2024-02-06 17:00:00 EET+0200 2024-02-06 19:00:00 EET+0200             27.8955
	          3 2024-02-06 17:00:00 EET+0200 2024-02-06 20:00:00 EET+0200           25.625667
	          4 2024-02-06 17:00:00 EET+0200 2024-02-06 21:00:00 EET+0200              24.024

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-07 00:00:00 EET+0200 2024-02-07 01:00:00 EET+0200              11.161
	          2 2024-02-06 13:00:00 EET+0200 2024-02-06 15:00:00 EET+0200             12.4005
	          3 2024-02-06 12:00:00 EET+0200 2024-02-06 15:00:00 EET+0200              12.401
	          4 2024-02-06 11:00:00 EET+0200 2024-02-06 15:00:00 EET+0200            12.40125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
