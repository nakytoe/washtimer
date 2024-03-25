
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-25 19:00:00 EET+0200 2024-03-25 20:00:00 EET+0200              21.347
	          2 2024-03-25 19:00:00 EET+0200 2024-03-25 21:00:00 EET+0200              19.958
	          3 2024-03-25 18:00:00 EET+0200 2024-03-25 21:00:00 EET+0200           17.929667
	          4 2024-03-25 18:00:00 EET+0200 2024-03-25 22:00:00 EET+0200             16.5555

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-27 00:00:00 EET+0200 2024-03-27 01:00:00 EET+0200               6.841
	          2 2024-03-26 23:00:00 EET+0200 2024-03-27 01:00:00 EET+0200               6.933
	          3 2024-03-26 22:00:00 EET+0200 2024-03-27 01:00:00 EET+0200            7.019667
	          4 2024-03-26 21:00:00 EET+0200 2024-03-27 01:00:00 EET+0200               7.074


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
