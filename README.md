
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-03 23:00:00 EET+0200 2024-03-04 00:00:00 EET+0200              12.239
	          2 2024-03-03 22:00:00 EET+0200 2024-03-04 00:00:00 EET+0200              11.504
	          3 2024-03-03 22:00:00 EET+0200 2024-03-04 01:00:00 EET+0200              10.857
	          4 2024-03-03 20:00:00 EET+0200 2024-03-04 00:00:00 EET+0200             10.8375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-03 06:00:00 EET+0200 2024-03-03 07:00:00 EET+0200               6.722
	          2 2024-03-03 06:00:00 EET+0200 2024-03-03 08:00:00 EET+0200                6.75
	          3 2024-03-03 06:00:00 EET+0200 2024-03-03 09:00:00 EET+0200            6.794333
	          4 2024-03-03 06:00:00 EET+0200 2024-03-03 10:00:00 EET+0200              6.7935


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
