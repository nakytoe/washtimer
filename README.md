
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-11 09:00:00 EET+0200 2023-12-11 10:00:00 EET+0200              23.328
	          2 2023-12-11 15:00:00 EET+0200 2023-12-11 17:00:00 EET+0200               21.36
	          3 2023-12-11 15:00:00 EET+0200 2023-12-11 18:00:00 EET+0200           20.743667
	          4 2023-12-11 14:00:00 EET+0200 2023-12-11 18:00:00 EET+0200             20.3565

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-12 00:00:00 EET+0200 2023-12-12 01:00:00 EET+0200              10.766
	          2 2023-12-11 23:00:00 EET+0200 2023-12-12 01:00:00 EET+0200             11.5035
	          3 2023-12-11 22:00:00 EET+0200 2023-12-12 01:00:00 EET+0200           12.580667
	          4 2023-12-11 21:00:00 EET+0200 2023-12-12 01:00:00 EET+0200             12.8735


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
