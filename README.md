
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-02 11:00:00 EET+0200 2024-02-02 12:00:00 EET+0200               3.222
	          2 2024-02-02 10:00:00 EET+0200 2024-02-02 12:00:00 EET+0200              3.1885
	          3 2024-02-02 10:00:00 EET+0200 2024-02-02 13:00:00 EET+0200               3.175
	          4 2024-02-02 09:00:00 EET+0200 2024-02-02 13:00:00 EET+0200             3.14825

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-02 03:00:00 EET+0200 2024-02-02 04:00:00 EET+0200              -0.176
	          2 2024-02-02 02:00:00 EET+0200 2024-02-02 04:00:00 EET+0200              -0.175
	          3 2024-02-02 02:00:00 EET+0200 2024-02-02 05:00:00 EET+0200           -0.174333
	          4 2024-02-02 01:00:00 EET+0200 2024-02-02 05:00:00 EET+0200             -0.1735


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
