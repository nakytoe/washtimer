
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-16 17:00:00 EET+0200 2023-11-16 18:00:00 EET+0200              24.123
	          2 2023-11-16 17:00:00 EET+0200 2023-11-16 19:00:00 EET+0200             23.3695
	          3 2023-11-16 16:00:00 EET+0200 2023-11-16 19:00:00 EET+0200           22.399333
	          4 2023-11-16 15:00:00 EET+0200 2023-11-16 19:00:00 EET+0200            21.91425

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-17 00:00:00 EET+0200 2023-11-17 01:00:00 EET+0200              10.468
	          2 2023-11-16 23:00:00 EET+0200 2023-11-17 01:00:00 EET+0200             11.8475
	          3 2023-11-16 22:00:00 EET+0200 2023-11-17 01:00:00 EET+0200              12.497
	          4 2023-11-16 21:00:00 EET+0200 2023-11-17 01:00:00 EET+0200            13.01875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
