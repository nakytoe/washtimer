
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-19 11:00:00 EET+0200 2023-12-19 12:00:00 EET+0200               4.083
	          2 2023-12-19 10:00:00 EET+0200 2023-12-19 12:00:00 EET+0200               3.999
	          3 2023-12-19 10:00:00 EET+0200 2023-12-19 13:00:00 EET+0200            3.947667
	          4 2023-12-19 09:00:00 EET+0200 2023-12-19 13:00:00 EET+0200                3.92

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-19 04:00:00 EET+0200 2023-12-19 05:00:00 EET+0200               0.196
	          2 2023-12-19 03:00:00 EET+0200 2023-12-19 05:00:00 EET+0200              0.2395
	          3 2023-12-19 03:00:00 EET+0200 2023-12-19 06:00:00 EET+0200            0.335333
	          4 2023-12-19 02:00:00 EET+0200 2023-12-19 06:00:00 EET+0200              0.4165


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
