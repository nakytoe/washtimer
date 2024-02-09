
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-09 16:00:00 EET+0200 2024-02-09 17:00:00 EET+0200                24.8
	          2 2024-02-09 22:00:00 EET+0200 2024-02-10 00:00:00 EET+0200             23.3015
	          3 2024-02-09 22:00:00 EET+0200 2024-02-10 01:00:00 EET+0200           22.278667
	          4 2024-02-09 22:00:00 EET+0200 2024-02-10 02:00:00 EET+0200              22.289

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-10 21:00:00 EET+0200 2024-02-10 22:00:00 EET+0200               9.914
	          2 2024-02-10 12:00:00 EET+0200 2024-02-10 14:00:00 EET+0200              11.124
	          3 2024-02-10 12:00:00 EET+0200 2024-02-10 15:00:00 EET+0200              11.343
	          4 2024-02-10 12:00:00 EET+0200 2024-02-10 16:00:00 EET+0200             11.5785


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
