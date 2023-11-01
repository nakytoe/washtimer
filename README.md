
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-01 18:00:00 EET+0200 2023-11-01 19:00:00 EET+0200               2.779
	          2 2023-11-01 18:00:00 EET+0200 2023-11-01 20:00:00 EET+0200              2.6215
	          3 2023-11-01 18:00:00 EET+0200 2023-11-01 21:00:00 EET+0200            2.561667
	          4 2023-11-01 18:00:00 EET+0200 2023-11-01 22:00:00 EET+0200               2.528

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-02 00:00:00 EET+0200 2023-11-02 01:00:00 EET+0200               2.102
	          2 2023-11-01 23:00:00 EET+0200 2023-11-02 01:00:00 EET+0200               2.236
	          3 2023-11-01 22:00:00 EET+0200 2023-11-02 01:00:00 EET+0200            2.319333
	          4 2023-11-01 21:00:00 EET+0200 2023-11-02 01:00:00 EET+0200             2.34625


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
