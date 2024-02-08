
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-08 07:00:00 EET+0200 2024-02-08 08:00:00 EET+0200              16.705
	          2 2024-02-08 06:00:00 EET+0200 2024-02-08 08:00:00 EET+0200               16.63
	          3 2024-02-08 07:00:00 EET+0200 2024-02-08 10:00:00 EET+0200              16.537
	          4 2024-02-08 06:00:00 EET+0200 2024-02-08 10:00:00 EET+0200             16.5415

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-08 12:00:00 EET+0200 2024-02-08 13:00:00 EET+0200              11.392
	          2 2024-02-08 11:00:00 EET+0200 2024-02-08 13:00:00 EET+0200              11.759
	          3 2024-02-08 11:00:00 EET+0200 2024-02-08 14:00:00 EET+0200           12.005667
	          4 2024-02-08 10:00:00 EET+0200 2024-02-08 14:00:00 EET+0200            12.52425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
