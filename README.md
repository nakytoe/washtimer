
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-10 17:00:00 EET+0200 2023-12-10 18:00:00 EET+0200              12.876
	          2 2023-12-10 17:00:00 EET+0200 2023-12-10 19:00:00 EET+0200             12.6155
	          3 2023-12-10 17:00:00 EET+0200 2023-12-10 20:00:00 EET+0200           12.531333
	          4 2023-12-10 16:00:00 EET+0200 2023-12-10 20:00:00 EET+0200            12.48675

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-10 07:00:00 EET+0200 2023-12-10 08:00:00 EET+0200               7.439
	          2 2023-12-10 06:00:00 EET+0200 2023-12-10 08:00:00 EET+0200               8.204
	          3 2023-12-10 06:00:00 EET+0200 2023-12-10 09:00:00 EET+0200            8.527667
	          4 2023-12-10 06:00:00 EET+0200 2023-12-10 10:00:00 EET+0200             8.87575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
