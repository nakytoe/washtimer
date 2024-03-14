
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-14 12:00:00 EET+0200 2024-03-14 13:00:00 EET+0200               3.798
	          2 2024-03-14 11:00:00 EET+0200 2024-03-14 13:00:00 EET+0200                3.78
	          3 2024-03-14 10:00:00 EET+0200 2024-03-14 13:00:00 EET+0200            3.765333
	          4 2024-03-14 09:00:00 EET+0200 2024-03-14 13:00:00 EET+0200             3.76925

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-15 00:00:00 EET+0200 2024-03-15 01:00:00 EET+0200              -0.009
	          2 2024-03-14 23:00:00 EET+0200 2024-03-15 01:00:00 EET+0200              0.0015
	          3 2024-03-14 22:00:00 EET+0200 2024-03-15 01:00:00 EET+0200            0.145333
	          4 2024-03-14 21:00:00 EET+0200 2024-03-15 01:00:00 EET+0200               0.551


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
