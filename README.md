
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-26 09:00:00 EET+0200 2024-03-26 10:00:00 EET+0200              17.514
	          2 2024-03-26 08:00:00 EET+0200 2024-03-26 10:00:00 EET+0200             17.3925
	          3 2024-03-26 08:00:00 EET+0200 2024-03-26 11:00:00 EET+0200           15.647667
	          4 2024-03-26 16:00:00 EET+0200 2024-03-26 20:00:00 EET+0200            14.71275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-27 00:00:00 EET+0200 2024-03-27 01:00:00 EET+0200               6.841
	          2 2024-03-26 23:00:00 EET+0200 2024-03-27 01:00:00 EET+0200               6.933
	          3 2024-03-26 22:00:00 EET+0200 2024-03-27 01:00:00 EET+0200            7.019667
	          4 2024-03-26 21:00:00 EET+0200 2024-03-27 01:00:00 EET+0200               7.074


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
