
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-28 08:00:00 EET+0200 2023-12-28 09:00:00 EET+0200              10.453
	          2 2023-12-28 08:00:00 EET+0200 2023-12-28 10:00:00 EET+0200              8.9785
	          3 2023-12-28 16:00:00 EET+0200 2023-12-28 19:00:00 EET+0200            8.639333
	          4 2023-12-28 16:00:00 EET+0200 2023-12-28 20:00:00 EET+0200               8.426

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-29 00:00:00 EET+0200 2023-12-29 01:00:00 EET+0200               3.195
	          2 2023-12-28 23:00:00 EET+0200 2023-12-29 01:00:00 EET+0200              3.5175
	          3 2023-12-28 22:00:00 EET+0200 2023-12-29 01:00:00 EET+0200            3.734667
	          4 2023-12-28 21:00:00 EET+0200 2023-12-29 01:00:00 EET+0200              3.9385


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
