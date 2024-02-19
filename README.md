
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-19 19:00:00 EET+0200 2024-02-19 20:00:00 EET+0200              11.756
	          2 2024-02-19 19:00:00 EET+0200 2024-02-19 21:00:00 EET+0200              10.693
	          3 2024-02-19 18:00:00 EET+0200 2024-02-19 21:00:00 EET+0200              10.227
	          4 2024-02-19 09:00:00 EET+0200 2024-02-19 13:00:00 EET+0200             9.86375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-19 06:00:00 EET+0200 2024-02-19 07:00:00 EET+0200               6.395
	          2 2024-02-19 23:00:00 EET+0200 2024-02-20 01:00:00 EET+0200              6.5825
	          3 2024-02-19 22:00:00 EET+0200 2024-02-20 01:00:00 EET+0200            6.709333
	          4 2024-02-19 21:00:00 EET+0200 2024-02-20 01:00:00 EET+0200              6.9155


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
