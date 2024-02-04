
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-04 19:00:00 EET+0200 2024-02-04 20:00:00 EET+0200               4.573
	          2 2024-02-04 19:00:00 EET+0200 2024-02-04 21:00:00 EET+0200               4.475
	          3 2024-02-04 18:00:00 EET+0200 2024-02-04 21:00:00 EET+0200            4.440333
	          4 2024-02-04 18:00:00 EET+0200 2024-02-04 22:00:00 EET+0200             4.23075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-04 06:00:00 EET+0200 2024-02-04 07:00:00 EET+0200               -0.01
	          2 2024-02-04 06:00:00 EET+0200 2024-02-04 08:00:00 EET+0200              -0.005
	          3 2024-02-04 06:00:00 EET+0200 2024-02-04 09:00:00 EET+0200                0.04
	          4 2024-02-04 06:00:00 EET+0200 2024-02-04 10:00:00 EET+0200               0.305


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
