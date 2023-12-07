
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-08 11:00:00 EET+0200 2023-12-08 12:00:00 EET+0200              14.725
	          2 2023-12-08 10:00:00 EET+0200 2023-12-08 12:00:00 EET+0200             14.7105
	          3 2023-12-08 10:00:00 EET+0200 2023-12-08 13:00:00 EET+0200           14.653333
	          4 2023-12-08 10:00:00 EET+0200 2023-12-08 14:00:00 EET+0200             14.6065

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-09 00:00:00 EET+0200 2023-12-09 01:00:00 EET+0200               8.679
	          2 2023-12-08 23:00:00 EET+0200 2023-12-09 01:00:00 EET+0200               8.879
	          3 2023-12-08 22:00:00 EET+0200 2023-12-09 01:00:00 EET+0200               9.327
	          4 2023-12-08 21:00:00 EET+0200 2023-12-09 01:00:00 EET+0200             9.93725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
