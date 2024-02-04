
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-05 08:00:00 EET+0200 2024-02-05 09:00:00 EET+0200               9.373
	          2 2024-02-05 08:00:00 EET+0200 2024-02-05 10:00:00 EET+0200                8.95
	          3 2024-02-05 07:00:00 EET+0200 2024-02-05 10:00:00 EET+0200            8.449667
	          4 2024-02-05 07:00:00 EET+0200 2024-02-05 11:00:00 EET+0200                 8.1

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-05 04:00:00 EET+0200 2024-02-05 05:00:00 EET+0200               0.619
	          2 2024-02-05 04:00:00 EET+0200 2024-02-05 06:00:00 EET+0200               0.744
	          3 2024-02-05 03:00:00 EET+0200 2024-02-05 06:00:00 EET+0200            0.895667
	          4 2024-02-05 02:00:00 EET+0200 2024-02-05 06:00:00 EET+0200               1.002


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
