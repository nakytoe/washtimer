
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
	          1 2024-02-14 03:00:00 EET+0200 2024-02-14 04:00:00 EET+0200               2.517
	          2 2024-02-14 02:00:00 EET+0200 2024-02-14 04:00:00 EET+0200              2.5315
	          3 2024-02-14 02:00:00 EET+0200 2024-02-14 05:00:00 EET+0200            2.679667
	          4 2024-02-14 01:00:00 EET+0200 2024-02-14 05:00:00 EET+0200             2.77825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
