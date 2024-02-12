
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-12 19:00:00 EET+0200 2024-02-12 20:00:00 EET+0200              11.534
	          2 2024-02-12 18:00:00 EET+0200 2024-02-12 20:00:00 EET+0200             11.4085
	          3 2024-02-12 18:00:00 EET+0200 2024-02-12 21:00:00 EET+0200           11.173667
	          4 2024-02-12 18:00:00 EET+0200 2024-02-12 22:00:00 EET+0200            10.75275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-14 00:00:00 EET+0200 2024-02-14 01:00:00 EET+0200                4.37
	          2 2024-02-13 23:00:00 EET+0200 2024-02-14 01:00:00 EET+0200              5.1665
	          3 2024-02-13 22:00:00 EET+0200 2024-02-14 01:00:00 EET+0200            5.473667
	          4 2024-02-13 21:00:00 EET+0200 2024-02-14 01:00:00 EET+0200             5.61475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
