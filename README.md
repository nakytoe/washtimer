
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-22 09:00:00 EET+0200 2024-02-22 10:00:00 EET+0200               8.059
	          2 2024-02-22 09:00:00 EET+0200 2024-02-22 11:00:00 EET+0200               8.059
	          3 2024-02-22 09:00:00 EET+0200 2024-02-22 12:00:00 EET+0200            7.851333
	          4 2024-02-22 09:00:00 EET+0200 2024-02-22 13:00:00 EET+0200             7.90325

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-23 00:00:00 EET+0200 2024-02-23 01:00:00 EET+0200               0.242
	          2 2024-02-22 23:00:00 EET+0200 2024-02-23 01:00:00 EET+0200              0.8685
	          3 2024-02-22 22:00:00 EET+0200 2024-02-23 01:00:00 EET+0200            1.589333
	          4 2024-02-22 21:00:00 EET+0200 2024-02-23 01:00:00 EET+0200              2.1225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
