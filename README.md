
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-31 16:00:00 EET+0200 2023-12-31 17:00:00 EET+0200              14.571
	          2 2023-12-31 15:00:00 EET+0200 2023-12-31 17:00:00 EET+0200              14.106
	          3 2023-12-31 15:00:00 EET+0200 2023-12-31 18:00:00 EET+0200           13.888333
	          4 2023-12-31 15:00:00 EET+0200 2023-12-31 19:00:00 EET+0200            13.48375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-31 05:00:00 EET+0200 2023-12-31 06:00:00 EET+0200               4.729
	          2 2023-12-31 05:00:00 EET+0200 2023-12-31 07:00:00 EET+0200               4.799
	          3 2023-12-31 04:00:00 EET+0200 2023-12-31 07:00:00 EET+0200               4.851
	          4 2023-12-31 04:00:00 EET+0200 2023-12-31 08:00:00 EET+0200              4.8785


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
