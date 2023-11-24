
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-24 11:00:00 EET+0200 2023-11-24 12:00:00 EET+0200               2.683
	          2 2023-11-24 11:00:00 EET+0200 2023-11-24 13:00:00 EET+0200              2.6435
	          3 2023-11-24 10:00:00 EET+0200 2023-11-24 13:00:00 EET+0200            2.624667
	          4 2023-11-24 09:00:00 EET+0200 2023-11-24 13:00:00 EET+0200               2.612

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-24 15:00:00 EET+0200 2023-11-24 16:00:00 EET+0200               -50.0
	          2 2023-11-24 15:00:00 EET+0200 2023-11-24 17:00:00 EET+0200               -50.0
	          3 2023-11-24 15:00:00 EET+0200 2023-11-24 18:00:00 EET+0200               -50.0
	          4 2023-11-24 15:00:00 EET+0200 2023-11-24 19:00:00 EET+0200               -50.0


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
