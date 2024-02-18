
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-18 18:00:00 EET+0200 2024-02-18 19:00:00 EET+0200               5.799
	          2 2024-02-18 17:00:00 EET+0200 2024-02-18 19:00:00 EET+0200               5.759
	          3 2024-02-18 16:00:00 EET+0200 2024-02-18 19:00:00 EET+0200               5.768
	          4 2024-02-18 16:00:00 EET+0200 2024-02-18 20:00:00 EET+0200              5.7535

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-18 06:00:00 EET+0200 2024-02-18 07:00:00 EET+0200               4.333
	          2 2024-02-18 06:00:00 EET+0200 2024-02-18 08:00:00 EET+0200               4.522
	          3 2024-02-18 06:00:00 EET+0200 2024-02-18 09:00:00 EET+0200               4.652
	          4 2024-02-18 06:00:00 EET+0200 2024-02-18 10:00:00 EET+0200             4.78325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
