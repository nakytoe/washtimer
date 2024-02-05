
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
	          1 2024-02-05 06:00:00 EET+0200 2024-02-05 07:00:00 EET+0200               5.131
	          2 2024-02-05 12:00:00 EET+0200 2024-02-05 14:00:00 EET+0200               5.692
	          3 2024-02-05 12:00:00 EET+0200 2024-02-05 15:00:00 EET+0200               5.801
	          4 2024-02-05 11:00:00 EET+0200 2024-02-05 15:00:00 EET+0200              5.9915


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
