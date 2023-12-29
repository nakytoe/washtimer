
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-29 18:00:00 EET+0200 2023-12-29 19:00:00 EET+0200               4.448
	          2 2023-12-29 18:00:00 EET+0200 2023-12-29 20:00:00 EET+0200              4.3395
	          3 2023-12-29 17:00:00 EET+0200 2023-12-29 20:00:00 EET+0200            4.257667
	          4 2023-12-29 17:00:00 EET+0200 2023-12-29 21:00:00 EET+0200             4.14675

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-30 00:00:00 EET+0200 2023-12-30 01:00:00 EET+0200               2.399
	          2 2023-12-29 23:00:00 EET+0200 2023-12-30 01:00:00 EET+0200              2.7705
	          3 2023-12-29 22:00:00 EET+0200 2023-12-30 01:00:00 EET+0200            3.009667
	          4 2023-12-29 21:00:00 EET+0200 2023-12-30 01:00:00 EET+0200             3.18775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
