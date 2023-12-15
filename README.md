
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-15 16:00:00 EET+0200 2023-12-15 17:00:00 EET+0200              24.801
	          2 2023-12-15 15:00:00 EET+0200 2023-12-15 17:00:00 EET+0200              22.982
	          3 2023-12-15 08:00:00 EET+0200 2023-12-15 11:00:00 EET+0200           22.815667
	          4 2023-12-15 08:00:00 EET+0200 2023-12-15 12:00:00 EET+0200            22.32025

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-16 00:00:00 EET+0200 2023-12-16 01:00:00 EET+0200               9.291
	          2 2023-12-15 23:00:00 EET+0200 2023-12-16 01:00:00 EET+0200              10.025
	          3 2023-12-15 22:00:00 EET+0200 2023-12-16 01:00:00 EET+0200              10.724
	          4 2023-12-15 21:00:00 EET+0200 2023-12-16 01:00:00 EET+0200            10.93725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
