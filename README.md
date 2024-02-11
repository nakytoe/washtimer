
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-11 15:00:00 EET+0200 2024-02-11 16:00:00 EET+0200                9.91
	          2 2024-02-11 18:00:00 EET+0200 2024-02-11 20:00:00 EET+0200              9.5675
	          3 2024-02-11 18:00:00 EET+0200 2024-02-11 21:00:00 EET+0200            9.312333
	          4 2024-02-11 15:00:00 EET+0200 2024-02-11 19:00:00 EET+0200             9.10875

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-11 06:00:00 EET+0200 2024-02-11 07:00:00 EET+0200               5.735
	          2 2024-02-11 06:00:00 EET+0200 2024-02-11 08:00:00 EET+0200              5.9175
	          3 2024-02-11 06:00:00 EET+0200 2024-02-11 09:00:00 EET+0200            6.142333
	          4 2024-02-11 06:00:00 EET+0200 2024-02-11 10:00:00 EET+0200              6.3135


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
