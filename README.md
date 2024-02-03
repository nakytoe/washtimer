
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-03 19:00:00 EET+0200 2024-02-03 20:00:00 EET+0200               1.288
	          2 2024-02-03 18:00:00 EET+0200 2024-02-03 20:00:00 EET+0200              1.2825
	          3 2024-02-03 18:00:00 EET+0200 2024-02-03 21:00:00 EET+0200            0.999667
	          4 2024-02-03 17:00:00 EET+0200 2024-02-03 21:00:00 EET+0200              0.8555

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-03 06:00:00 EET+0200 2024-02-03 07:00:00 EET+0200              -0.183
	          2 2024-02-03 06:00:00 EET+0200 2024-02-03 08:00:00 EET+0200              -0.112
	          3 2024-02-03 06:00:00 EET+0200 2024-02-03 09:00:00 EET+0200           -0.076667
	          4 2024-02-03 06:00:00 EET+0200 2024-02-03 10:00:00 EET+0200            -0.05725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
