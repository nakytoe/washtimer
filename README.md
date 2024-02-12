
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-12 09:00:00 EET+0200 2024-02-12 10:00:00 EET+0200              12.522
	          2 2024-02-12 09:00:00 EET+0200 2024-02-12 11:00:00 EET+0200             12.0705
	          3 2024-02-12 07:00:00 EET+0200 2024-02-12 10:00:00 EET+0200           11.827333
	          4 2024-02-12 07:00:00 EET+0200 2024-02-12 11:00:00 EET+0200            11.77525

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-13 00:00:00 EET+0200 2024-02-13 01:00:00 EET+0200               7.108
	          2 2024-02-12 23:00:00 EET+0200 2024-02-13 01:00:00 EET+0200              7.5065
	          3 2024-02-12 22:00:00 EET+0200 2024-02-13 01:00:00 EET+0200            7.812667
	          4 2024-02-12 13:00:00 EET+0200 2024-02-12 17:00:00 EET+0200             8.10675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
