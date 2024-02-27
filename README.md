
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-27 15:00:00 EET+0200 2024-02-27 16:00:00 EET+0200               7.997
	          2 2024-02-27 15:00:00 EET+0200 2024-02-27 17:00:00 EET+0200               7.533
	          3 2024-02-27 15:00:00 EET+0200 2024-02-27 18:00:00 EET+0200               7.471
	          4 2024-02-27 15:00:00 EET+0200 2024-02-27 19:00:00 EET+0200               7.462

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-28 03:00:00 EET+0200 2024-02-28 04:00:00 EET+0200               2.053
	          2 2024-02-28 03:00:00 EET+0200 2024-02-28 05:00:00 EET+0200              2.0565
	          3 2024-02-28 02:00:00 EET+0200 2024-02-28 05:00:00 EET+0200            2.065667
	          4 2024-02-28 01:00:00 EET+0200 2024-02-28 05:00:00 EET+0200               2.081


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
