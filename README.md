
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-06 19:00:00 EET+0200 2024-03-06 20:00:00 EET+0200              14.787
	          2 2024-03-06 19:00:00 EET+0200 2024-03-06 21:00:00 EET+0200             14.7735
	          3 2024-03-06 18:00:00 EET+0200 2024-03-06 21:00:00 EET+0200           14.231667
	          4 2024-03-06 18:00:00 EET+0200 2024-03-06 22:00:00 EET+0200            13.55525

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-06 15:00:00 EET+0200 2024-03-06 16:00:00 EET+0200               8.759
	          2 2024-03-06 14:00:00 EET+0200 2024-03-06 16:00:00 EET+0200               8.903
	          3 2024-03-06 14:00:00 EET+0200 2024-03-06 17:00:00 EET+0200            9.053667
	          4 2024-03-06 13:00:00 EET+0200 2024-03-06 17:00:00 EET+0200             9.34225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
