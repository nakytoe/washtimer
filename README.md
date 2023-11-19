
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-19 19:00:00 EET+0200 2023-11-19 20:00:00 EET+0200              12.796
	          2 2023-11-19 19:00:00 EET+0200 2023-11-19 21:00:00 EET+0200              12.698
	          3 2023-11-19 18:00:00 EET+0200 2023-11-19 21:00:00 EET+0200           12.392667
	          4 2023-11-19 18:00:00 EET+0200 2023-11-19 22:00:00 EET+0200            12.04275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-19 06:00:00 EET+0200 2023-11-19 07:00:00 EET+0200               4.662
	          2 2023-11-19 06:00:00 EET+0200 2023-11-19 08:00:00 EET+0200              4.9215
	          3 2023-11-19 06:00:00 EET+0200 2023-11-19 09:00:00 EET+0200            5.107667
	          4 2023-11-19 06:00:00 EET+0200 2023-11-19 10:00:00 EET+0200             5.30725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
