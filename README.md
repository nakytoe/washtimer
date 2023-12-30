
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-30 19:00:00 EET+0200 2023-12-30 20:00:00 EET+0200               9.919
	          2 2023-12-30 18:00:00 EET+0200 2023-12-30 20:00:00 EET+0200              9.9145
	          3 2023-12-30 18:00:00 EET+0200 2023-12-30 21:00:00 EET+0200               9.548
	          4 2023-12-30 17:00:00 EET+0200 2023-12-30 21:00:00 EET+0200             9.33075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-30 06:00:00 EET+0200 2023-12-30 07:00:00 EET+0200               2.499
	          2 2023-12-30 06:00:00 EET+0200 2023-12-30 08:00:00 EET+0200              2.6145
	          3 2023-12-30 06:00:00 EET+0200 2023-12-30 09:00:00 EET+0200            2.788333
	          4 2023-12-30 06:00:00 EET+0200 2023-12-30 10:00:00 EET+0200             2.98425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
