
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-17 19:00:00 EET+0200 2023-12-17 20:00:00 EET+0200               1.721
	          2 2023-12-17 19:00:00 EET+0200 2023-12-17 21:00:00 EET+0200              1.7055
	          3 2023-12-17 19:00:00 EET+0200 2023-12-17 22:00:00 EET+0200            1.649667
	          4 2023-12-17 19:00:00 EET+0200 2023-12-17 23:00:00 EET+0200              1.5915

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-17 06:00:00 EET+0200 2023-12-17 07:00:00 EET+0200              -0.011
	          2 2023-12-17 06:00:00 EET+0200 2023-12-17 08:00:00 EET+0200              -0.006
	          3 2023-12-17 06:00:00 EET+0200 2023-12-17 09:00:00 EET+0200           -0.003667
	          4 2023-12-17 06:00:00 EET+0200 2023-12-17 10:00:00 EET+0200             0.03725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
