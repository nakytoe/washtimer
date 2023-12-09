
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-09 15:00:00 EET+0200 2023-12-09 16:00:00 EET+0200              10.618
	          2 2023-12-09 15:00:00 EET+0200 2023-12-09 17:00:00 EET+0200              10.486
	          3 2023-12-09 15:00:00 EET+0200 2023-12-09 18:00:00 EET+0200           10.300667
	          4 2023-12-09 14:00:00 EET+0200 2023-12-09 18:00:00 EET+0200             10.2055

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-10 00:00:00 EET+0200 2023-12-10 01:00:00 EET+0200               5.726
	          2 2023-12-09 23:00:00 EET+0200 2023-12-10 01:00:00 EET+0200               6.387
	          3 2023-12-09 22:00:00 EET+0200 2023-12-10 01:00:00 EET+0200               6.755
	          4 2023-12-09 21:00:00 EET+0200 2023-12-10 01:00:00 EET+0200              7.0645


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
