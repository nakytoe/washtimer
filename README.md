
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-18 09:00:00 EET+0200 2023-12-18 10:00:00 EET+0200               3.099
	          2 2023-12-18 09:00:00 EET+0200 2023-12-18 11:00:00 EET+0200               2.996
	          3 2023-12-18 09:00:00 EET+0200 2023-12-18 12:00:00 EET+0200            2.884333
	          4 2023-12-18 08:00:00 EET+0200 2023-12-18 12:00:00 EET+0200             2.82075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-18 06:00:00 EET+0200 2023-12-18 07:00:00 EET+0200               1.249
	          2 2023-12-18 23:00:00 EET+0200 2023-12-19 01:00:00 EET+0200                1.41
	          3 2023-12-18 22:00:00 EET+0200 2023-12-19 01:00:00 EET+0200            1.568667
	          4 2023-12-18 21:00:00 EET+0200 2023-12-19 01:00:00 EET+0200             1.70975


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
