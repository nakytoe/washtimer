
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-15 18:00:00 EET+0200 2024-02-15 19:00:00 EET+0200              10.169
	          2 2024-02-15 18:00:00 EET+0200 2024-02-15 20:00:00 EET+0200              10.169
	          3 2024-02-15 17:00:00 EET+0200 2024-02-15 20:00:00 EET+0200            9.939333
	          4 2024-02-15 16:00:00 EET+0200 2024-02-15 20:00:00 EET+0200             9.71375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-15 00:00:00 EET+0200 2024-02-15 01:00:00 EET+0200               5.638
	          2 2024-02-15 00:00:00 EET+0200 2024-02-15 02:00:00 EET+0200              5.7125
	          3 2024-02-15 00:00:00 EET+0200 2024-02-15 03:00:00 EET+0200               5.724
	          4 2024-02-15 00:00:00 EET+0200 2024-02-15 04:00:00 EET+0200             5.75525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
