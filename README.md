
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-22 20:00:00 EET+0200 2024-03-22 21:00:00 EET+0200               7.407
	          2 2024-03-22 19:00:00 EET+0200 2024-03-22 21:00:00 EET+0200               7.393
	          3 2024-03-22 18:00:00 EET+0200 2024-03-22 21:00:00 EET+0200            7.327333
	          4 2024-03-22 18:00:00 EET+0200 2024-03-22 22:00:00 EET+0200              7.1705

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-22 06:00:00 EET+0200 2024-03-22 07:00:00 EET+0200               4.581
	          2 2024-03-22 06:00:00 EET+0200 2024-03-22 08:00:00 EET+0200              4.9145
	          3 2024-03-22 06:00:00 EET+0200 2024-03-22 09:00:00 EET+0200            5.262333
	          4 2024-03-22 06:00:00 EET+0200 2024-03-22 10:00:00 EET+0200               5.597


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
