
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-26 19:00:00 EET+0200 2023-12-26 20:00:00 EET+0200               6.566
	          2 2023-12-26 18:00:00 EET+0200 2023-12-26 20:00:00 EET+0200              6.5615
	          3 2023-12-26 18:00:00 EET+0200 2023-12-26 21:00:00 EET+0200               6.417
	          4 2023-12-26 17:00:00 EET+0200 2023-12-26 21:00:00 EET+0200               6.284

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-26 06:00:00 EET+0200 2023-12-26 07:00:00 EET+0200               4.156
	          2 2023-12-26 06:00:00 EET+0200 2023-12-26 08:00:00 EET+0200              4.1765
	          3 2023-12-26 06:00:00 EET+0200 2023-12-26 09:00:00 EET+0200            4.299333
	          4 2023-12-26 06:00:00 EET+0200 2023-12-26 10:00:00 EET+0200             4.43475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
