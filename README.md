
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-12 19:00:00 EET+0200 2023-11-12 20:00:00 EET+0200               4.961
	          2 2023-11-12 18:00:00 EET+0200 2023-11-12 20:00:00 EET+0200              4.9605
	          3 2023-11-12 18:00:00 EET+0200 2023-11-12 21:00:00 EET+0200            4.922333
	          4 2023-11-12 17:00:00 EET+0200 2023-11-12 21:00:00 EET+0200              4.8455

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-12 07:00:00 EET+0200 2023-11-12 08:00:00 EET+0200               2.543
	          2 2023-11-12 06:00:00 EET+0200 2023-11-12 08:00:00 EET+0200               2.595
	          3 2023-11-12 06:00:00 EET+0200 2023-11-12 09:00:00 EET+0200               2.625
	          4 2023-11-12 06:00:00 EET+0200 2023-11-12 10:00:00 EET+0200              2.6765


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
