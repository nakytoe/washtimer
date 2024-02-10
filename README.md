
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-10 06:00:00 EET+0200 2024-02-10 07:00:00 EET+0200              19.219
	          2 2024-02-10 06:00:00 EET+0200 2024-02-10 08:00:00 EET+0200             17.9795
	          3 2024-02-10 06:00:00 EET+0200 2024-02-10 09:00:00 EET+0200           16.946333
	          4 2024-02-10 06:00:00 EET+0200 2024-02-10 10:00:00 EET+0200             16.0495

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-10 21:00:00 EET+0200 2024-02-10 22:00:00 EET+0200               9.914
	          2 2024-02-10 12:00:00 EET+0200 2024-02-10 14:00:00 EET+0200              11.124
	          3 2024-02-10 12:00:00 EET+0200 2024-02-10 15:00:00 EET+0200              11.343
	          4 2024-02-10 12:00:00 EET+0200 2024-02-10 16:00:00 EET+0200             11.5785


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
