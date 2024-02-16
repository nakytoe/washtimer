
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-16 08:00:00 EET+0200 2024-02-16 09:00:00 EET+0200               4.845
	          2 2024-02-16 08:00:00 EET+0200 2024-02-16 10:00:00 EET+0200              4.8335
	          3 2024-02-16 08:00:00 EET+0200 2024-02-16 11:00:00 EET+0200            4.796333
	          4 2024-02-16 07:00:00 EET+0200 2024-02-16 11:00:00 EET+0200             4.70725

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-17 00:00:00 EET+0200 2024-02-17 01:00:00 EET+0200               2.425
	          2 2024-02-16 23:00:00 EET+0200 2024-02-17 01:00:00 EET+0200               2.727
	          3 2024-02-16 22:00:00 EET+0200 2024-02-17 01:00:00 EET+0200            2.872333
	          4 2024-02-16 21:00:00 EET+0200 2024-02-17 01:00:00 EET+0200              2.9715


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
