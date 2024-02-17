
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-17 19:00:00 EET+0200 2024-02-17 20:00:00 EET+0200               3.275
	          2 2024-02-17 18:00:00 EET+0200 2024-02-17 20:00:00 EET+0200                3.27
	          3 2024-02-17 18:00:00 EET+0200 2024-02-17 21:00:00 EET+0200               3.249
	          4 2024-02-17 18:00:00 EET+0200 2024-02-17 22:00:00 EET+0200             3.23325

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-17 06:00:00 EET+0200 2024-02-17 07:00:00 EET+0200               1.239
	          2 2024-02-17 06:00:00 EET+0200 2024-02-17 08:00:00 EET+0200              1.3085
	          3 2024-02-17 06:00:00 EET+0200 2024-02-17 09:00:00 EET+0200            1.584667
	          4 2024-02-17 12:00:00 EET+0200 2024-02-17 16:00:00 EET+0200             1.71525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
