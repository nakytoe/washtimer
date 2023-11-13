
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-13 10:00:00 EET+0200 2023-11-13 11:00:00 EET+0200              15.159
	          2 2023-11-13 09:00:00 EET+0200 2023-11-13 11:00:00 EET+0200              14.972
	          3 2023-11-13 09:00:00 EET+0200 2023-11-13 12:00:00 EET+0200           14.751667
	          4 2023-11-13 09:00:00 EET+0200 2023-11-13 13:00:00 EET+0200            14.09225

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-14 00:00:00 EET+0200 2023-11-14 01:00:00 EET+0200               3.721
	          2 2023-11-13 23:00:00 EET+0200 2023-11-14 01:00:00 EET+0200              4.1735
	          3 2023-11-13 22:00:00 EET+0200 2023-11-14 01:00:00 EET+0200               4.558
	          4 2023-11-13 21:00:00 EET+0200 2023-11-14 01:00:00 EET+0200             4.86175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
