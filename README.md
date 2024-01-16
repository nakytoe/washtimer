
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-16 09:00:00 EET+0200 2024-01-16 10:00:00 EET+0200              34.173
	          2 2024-01-16 09:00:00 EET+0200 2024-01-16 11:00:00 EET+0200              33.861
	          3 2024-01-16 09:00:00 EET+0200 2024-01-16 12:00:00 EET+0200           32.904333
	          4 2024-01-16 09:00:00 EET+0200 2024-01-16 13:00:00 EET+0200            30.89525

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-16 06:00:00 EET+0200 2024-01-16 07:00:00 EET+0200              10.348
	          2 2024-01-16 06:00:00 EET+0200 2024-01-16 08:00:00 EET+0200                12.8
	          3 2024-01-16 22:00:00 EET+0200 2024-01-17 01:00:00 EET+0200           14.673667
	          4 2024-01-16 21:00:00 EET+0200 2024-01-17 01:00:00 EET+0200              15.702


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
