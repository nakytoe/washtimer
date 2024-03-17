
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-17 19:00:00 EET+0200 2024-03-17 20:00:00 EET+0200              11.413
	          2 2024-03-17 19:00:00 EET+0200 2024-03-17 21:00:00 EET+0200              11.011
	          3 2024-03-17 18:00:00 EET+0200 2024-03-17 21:00:00 EET+0200           10.365333
	          4 2024-03-17 18:00:00 EET+0200 2024-03-17 22:00:00 EET+0200              9.6655

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-18 04:00:00 EET+0200 2024-03-18 05:00:00 EET+0200               4.842
	          2 2024-03-18 04:00:00 EET+0200 2024-03-18 06:00:00 EET+0200                4.87
	          3 2024-03-18 03:00:00 EET+0200 2024-03-18 06:00:00 EET+0200               4.896
	          4 2024-03-18 02:00:00 EET+0200 2024-03-18 06:00:00 EET+0200             4.94775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
