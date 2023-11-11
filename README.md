
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-11 19:00:00 EET+0200 2023-11-11 20:00:00 EET+0200               3.958
	          2 2023-11-11 18:00:00 EET+0200 2023-11-11 20:00:00 EET+0200               3.944
	          3 2023-11-11 17:00:00 EET+0200 2023-11-11 20:00:00 EET+0200            3.905333
	          4 2023-11-11 17:00:00 EET+0200 2023-11-11 21:00:00 EET+0200             3.84825

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-11 06:00:00 EET+0200 2023-11-11 07:00:00 EET+0200               2.533
	          2 2023-11-11 06:00:00 EET+0200 2023-11-11 08:00:00 EET+0200              2.5685
	          3 2023-11-11 06:00:00 EET+0200 2023-11-11 09:00:00 EET+0200            2.640667
	          4 2023-11-11 06:00:00 EET+0200 2023-11-11 10:00:00 EET+0200             2.76875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
