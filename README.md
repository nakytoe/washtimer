
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-18 09:00:00 EET+0200 2024-03-18 10:00:00 EET+0200              11.337
	          2 2024-03-18 09:00:00 EET+0200 2024-03-18 11:00:00 EET+0200             10.5335
	          3 2024-03-18 09:00:00 EET+0200 2024-03-18 12:00:00 EET+0200            9.912667
	          4 2024-03-18 09:00:00 EET+0200 2024-03-18 13:00:00 EET+0200             9.39225

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-18 06:00:00 EET+0200 2024-03-18 07:00:00 EET+0200               5.116
	          2 2024-03-18 06:00:00 EET+0200 2024-03-18 08:00:00 EET+0200              5.2365
	          3 2024-03-18 06:00:00 EET+0200 2024-03-18 09:00:00 EET+0200            5.464333
	          4 2024-03-18 21:00:00 EET+0200 2024-03-19 01:00:00 EET+0200              5.7835


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
