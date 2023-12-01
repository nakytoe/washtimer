
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-01 16:00:00 EET+0200 2023-12-01 17:00:00 EET+0200              18.235
	          2 2023-12-01 15:00:00 EET+0200 2023-12-01 17:00:00 EET+0200             18.0615
	          3 2023-12-01 14:00:00 EET+0200 2023-12-01 17:00:00 EET+0200              17.414
	          4 2023-12-01 13:00:00 EET+0200 2023-12-01 17:00:00 EET+0200             17.0905

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-01 06:00:00 EET+0200 2023-12-01 07:00:00 EET+0200               9.919
	          2 2023-12-01 06:00:00 EET+0200 2023-12-01 08:00:00 EET+0200             12.1595
	          3 2023-12-01 09:00:00 EET+0200 2023-12-01 12:00:00 EET+0200              13.457
	          4 2023-12-01 06:00:00 EET+0200 2023-12-01 10:00:00 EET+0200             13.9665


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
