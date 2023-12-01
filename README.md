
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-01 16:00:00 EET+0200 2023-12-01 17:00:00 EET+0200              18.235
	          2 2023-12-01 15:00:00 EET+0200 2023-12-01 17:00:00 EET+0200             18.0615
	          3 2023-12-01 15:00:00 EET+0200 2023-12-01 18:00:00 EET+0200              17.414
	          4 2023-12-02 17:00:00 EET+0200 2023-12-02 21:00:00 EET+0200            16.99875

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-02 04:00:00 EET+0200 2023-12-02 05:00:00 EET+0200              11.156
	          2 2023-12-02 03:00:00 EET+0200 2023-12-02 05:00:00 EET+0200              11.254
	          3 2023-12-02 03:00:00 EET+0200 2023-12-02 06:00:00 EET+0200           11.434333
	          4 2023-12-02 03:00:00 EET+0200 2023-12-02 07:00:00 EET+0200              11.543


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
