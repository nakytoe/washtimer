
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-14 12:00:00 EET+0200 2023-11-14 13:00:00 EET+0200              18.609
	          2 2023-11-14 12:00:00 EET+0200 2023-11-14 14:00:00 EET+0200              18.608
	          3 2023-11-14 11:00:00 EET+0200 2023-11-14 14:00:00 EET+0200           17.986667
	          4 2023-11-14 10:00:00 EET+0200 2023-11-14 14:00:00 EET+0200            17.33525

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-14 00:00:00 EET+0200 2023-11-14 01:00:00 EET+0200               3.721
	          2 2023-11-14 00:00:00 EET+0200 2023-11-14 02:00:00 EET+0200              4.1425
	          3 2023-11-13 23:00:00 EET+0200 2023-11-14 02:00:00 EET+0200            4.303667
	          4 2023-11-13 23:00:00 EET+0200 2023-11-14 03:00:00 EET+0200              4.4085


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
