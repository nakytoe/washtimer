
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-28 12:00:00 EET+0200 2023-11-28 13:00:00 EET+0200               9.663
	          2 2023-11-28 12:00:00 EET+0200 2023-11-28 14:00:00 EET+0200               9.611
	          3 2023-11-28 12:00:00 EET+0200 2023-11-28 15:00:00 EET+0200               9.304
	          4 2023-11-28 11:00:00 EET+0200 2023-11-28 15:00:00 EET+0200             8.79025

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-29 00:00:00 EET+0200 2023-11-29 01:00:00 EET+0200               2.559
	          2 2023-11-28 23:00:00 EET+0200 2023-11-29 01:00:00 EET+0200               2.688
	          3 2023-11-28 22:00:00 EET+0200 2023-11-29 01:00:00 EET+0200            2.825667
	          4 2023-11-28 21:00:00 EET+0200 2023-11-29 01:00:00 EET+0200             2.92475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
