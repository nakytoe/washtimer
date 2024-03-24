
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-24 19:00:00 EET+0200 2024-03-24 20:00:00 EET+0200                 9.3
	          2 2024-03-24 19:00:00 EET+0200 2024-03-24 21:00:00 EET+0200               9.294
	          3 2024-03-24 19:00:00 EET+0200 2024-03-24 22:00:00 EET+0200            8.961333
	          4 2024-03-24 19:00:00 EET+0200 2024-03-24 23:00:00 EET+0200             8.72875

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-24 07:00:00 EET+0200 2024-03-24 08:00:00 EET+0200               4.113
	          2 2024-03-24 06:00:00 EET+0200 2024-03-24 08:00:00 EET+0200              4.3095
	          3 2024-03-24 06:00:00 EET+0200 2024-03-24 09:00:00 EET+0200               4.412
	          4 2024-03-24 06:00:00 EET+0200 2024-03-24 10:00:00 EET+0200              4.6085


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
