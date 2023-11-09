
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-09 14:00:00 EET+0200 2023-11-09 15:00:00 EET+0200              15.924
	          2 2023-11-09 08:00:00 EET+0200 2023-11-09 10:00:00 EET+0200              14.987
	          3 2023-11-09 08:00:00 EET+0200 2023-11-09 11:00:00 EET+0200           14.523667
	          4 2023-11-09 07:00:00 EET+0200 2023-11-09 11:00:00 EET+0200            14.29075

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-10 00:00:00 EET+0200 2023-11-10 01:00:00 EET+0200               3.529
	          2 2023-11-09 23:00:00 EET+0200 2023-11-10 01:00:00 EET+0200              3.8215
	          3 2023-11-09 22:00:00 EET+0200 2023-11-10 01:00:00 EET+0200            4.082333
	          4 2023-11-09 21:00:00 EET+0200 2023-11-10 01:00:00 EET+0200              4.2685


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
