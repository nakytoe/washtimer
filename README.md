
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-25 18:00:00 EET+0200 2024-01-25 19:00:00 EET+0200              15.171
	          2 2024-01-25 18:00:00 EET+0200 2024-01-25 20:00:00 EET+0200              14.672
	          3 2024-01-25 17:00:00 EET+0200 2024-01-25 20:00:00 EET+0200           13.971667
	          4 2024-01-25 17:00:00 EET+0200 2024-01-25 21:00:00 EET+0200            13.54125

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-25 06:00:00 EET+0200 2024-01-25 07:00:00 EET+0200               6.325
	          2 2024-01-25 06:00:00 EET+0200 2024-01-25 08:00:00 EET+0200              7.7715
	          3 2024-01-25 06:00:00 EET+0200 2024-01-25 09:00:00 EET+0200            8.292667
	          4 2024-01-25 06:00:00 EET+0200 2024-01-25 10:00:00 EET+0200               8.979


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
