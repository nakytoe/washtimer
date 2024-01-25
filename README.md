
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-26 08:00:00 EET+0200 2024-01-26 09:00:00 EET+0200              18.089
	          2 2024-01-26 08:00:00 EET+0200 2024-01-26 10:00:00 EET+0200              17.818
	          3 2024-01-26 08:00:00 EET+0200 2024-01-26 11:00:00 EET+0200           17.493333
	          4 2024-01-26 07:00:00 EET+0200 2024-01-26 11:00:00 EET+0200             17.2945

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-27 00:00:00 EET+0200 2024-01-27 01:00:00 EET+0200               2.726
	          2 2024-01-26 23:00:00 EET+0200 2024-01-27 01:00:00 EET+0200               2.875
	          3 2024-01-26 22:00:00 EET+0200 2024-01-27 01:00:00 EET+0200            2.981333
	          4 2024-01-26 21:00:00 EET+0200 2024-01-27 01:00:00 EET+0200               3.091


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
