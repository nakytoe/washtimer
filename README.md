
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-21 10:00:00 EET+0200 2024-02-21 11:00:00 EET+0200               6.966
	          2 2024-02-21 10:00:00 EET+0200 2024-02-21 12:00:00 EET+0200              6.9275
	          3 2024-02-21 10:00:00 EET+0200 2024-02-21 13:00:00 EET+0200               6.906
	          4 2024-02-21 09:00:00 EET+0200 2024-02-21 13:00:00 EET+0200             6.89375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-22 00:00:00 EET+0200 2024-02-22 01:00:00 EET+0200               4.263
	          2 2024-02-21 23:00:00 EET+0200 2024-02-22 01:00:00 EET+0200              4.5725
	          3 2024-02-21 22:00:00 EET+0200 2024-02-22 01:00:00 EET+0200            4.748667
	          4 2024-02-21 21:00:00 EET+0200 2024-02-22 01:00:00 EET+0200              4.9885


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
