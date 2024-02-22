
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-22 15:00:00 EET+0200 2024-02-22 16:00:00 EET+0200               4.333
	          2 2024-02-22 15:00:00 EET+0200 2024-02-22 17:00:00 EET+0200              4.3025
	          3 2024-02-22 15:00:00 EET+0200 2024-02-22 18:00:00 EET+0200            4.278667
	          4 2024-02-22 15:00:00 EET+0200 2024-02-22 19:00:00 EET+0200             4.26725

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-24 00:00:00 EET+0200 2024-02-24 01:00:00 EET+0200              -0.098
	          2 2024-02-23 23:00:00 EET+0200 2024-02-24 01:00:00 EET+0200             -0.0565
	          3 2024-02-23 22:00:00 EET+0200 2024-02-24 01:00:00 EET+0200           -0.040667
	          4 2024-02-23 21:00:00 EET+0200 2024-02-24 01:00:00 EET+0200             -0.0305


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
