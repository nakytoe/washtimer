
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-03 07:00:00 EET+0200 2023-11-03 08:00:00 EET+0200                4.96
	          2 2023-11-03 07:00:00 EET+0200 2023-11-03 09:00:00 EET+0200              4.0305
	          3 2023-11-03 06:00:00 EET+0200 2023-11-03 09:00:00 EET+0200            3.662333
	          4 2023-11-03 06:00:00 EET+0200 2023-11-03 10:00:00 EET+0200             3.38225

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-04 00:00:00 EET+0200 2023-11-04 01:00:00 EET+0200                 0.3
	          2 2023-11-03 23:00:00 EET+0200 2023-11-04 01:00:00 EET+0200              0.4575
	          3 2023-11-03 22:00:00 EET+0200 2023-11-04 01:00:00 EET+0200            0.718667
	          4 2023-11-03 21:00:00 EET+0200 2023-11-04 01:00:00 EET+0200               0.914


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
