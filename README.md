
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-09 08:00:00 EET+0200 2024-02-09 09:00:00 EET+0200              30.993
	          2 2024-02-09 08:00:00 EET+0200 2024-02-09 10:00:00 EET+0200             30.8985
	          3 2024-02-09 08:00:00 EET+0200 2024-02-09 11:00:00 EET+0200           28.865333
	          4 2024-02-09 07:00:00 EET+0200 2024-02-09 11:00:00 EET+0200            27.68275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-09 12:00:00 EET+0200 2024-02-09 13:00:00 EET+0200              11.913
	          2 2024-02-09 12:00:00 EET+0200 2024-02-09 14:00:00 EET+0200             12.3415
	          3 2024-02-09 12:00:00 EET+0200 2024-02-09 15:00:00 EET+0200           13.055333
	          4 2024-02-09 11:00:00 EET+0200 2024-02-09 15:00:00 EET+0200            13.64025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
