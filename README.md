
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-05 06:00:00 EET+0200 2024-03-05 07:00:00 EET+0200              14.355
	          2 2024-03-05 06:00:00 EET+0200 2024-03-05 08:00:00 EET+0200             14.0125
	          3 2024-03-05 06:00:00 EET+0200 2024-03-05 09:00:00 EET+0200              13.682
	          4 2024-03-05 06:00:00 EET+0200 2024-03-05 10:00:00 EET+0200            13.82675

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-05 04:00:00 EET+0200 2024-03-05 05:00:00 EET+0200               6.989
	          2 2024-03-05 03:00:00 EET+0200 2024-03-05 05:00:00 EET+0200               6.995
	          3 2024-03-05 02:00:00 EET+0200 2024-03-05 05:00:00 EET+0200                7.16
	          4 2024-03-05 02:00:00 EET+0200 2024-03-05 06:00:00 EET+0200               7.456


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
