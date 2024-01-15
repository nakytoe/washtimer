
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
	          1 2024-01-16 05:00:00 EET+0200 2024-01-16 06:00:00 EET+0200               9.621
	          2 2024-01-16 04:00:00 EET+0200 2024-01-16 06:00:00 EET+0200              9.6625
	          3 2024-01-16 03:00:00 EET+0200 2024-01-16 06:00:00 EET+0200            9.751333
	          4 2024-01-16 02:00:00 EET+0200 2024-01-16 06:00:00 EET+0200               9.837


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
