
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-14 12:00:00 EET+0200 2024-02-14 13:00:00 EET+0200                6.37
	          2 2024-02-14 12:00:00 EET+0200 2024-02-14 14:00:00 EET+0200              6.3635
	          3 2024-02-14 12:00:00 EET+0200 2024-02-14 15:00:00 EET+0200            6.345333
	          4 2024-02-14 11:00:00 EET+0200 2024-02-14 15:00:00 EET+0200              6.3115

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-14 06:00:00 EET+0200 2024-02-14 07:00:00 EET+0200               4.437
	          2 2024-02-14 06:00:00 EET+0200 2024-02-14 08:00:00 EET+0200               5.123
	          3 2024-02-14 06:00:00 EET+0200 2024-02-14 09:00:00 EET+0200            5.444333
	          4 2024-02-14 06:00:00 EET+0200 2024-02-14 10:00:00 EET+0200             5.63175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
