
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-27 09:00:00 EET+0200 2023-11-27 10:00:00 EET+0200              17.979
	          2 2023-11-27 09:00:00 EET+0200 2023-11-27 11:00:00 EET+0200              17.633
	          3 2023-11-27 08:00:00 EET+0200 2023-11-27 11:00:00 EET+0200           17.497333
	          4 2023-11-27 08:00:00 EET+0200 2023-11-27 12:00:00 EET+0200              17.401

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-28 00:00:00 EET+0200 2023-11-28 01:00:00 EET+0200               3.711
	          2 2023-11-27 23:00:00 EET+0200 2023-11-28 01:00:00 EET+0200              4.3355
	          3 2023-11-27 22:00:00 EET+0200 2023-11-28 01:00:00 EET+0200            5.325333
	          4 2023-11-27 21:00:00 EET+0200 2023-11-28 01:00:00 EET+0200             5.76725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
