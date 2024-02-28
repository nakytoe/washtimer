
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-28 18:00:00 EET+0200 2024-02-28 19:00:00 EET+0200               2.831
	          2 2024-02-28 17:00:00 EET+0200 2024-02-28 19:00:00 EET+0200              2.8045
	          3 2024-02-28 17:00:00 EET+0200 2024-02-28 20:00:00 EET+0200            2.794667
	          4 2024-02-28 16:00:00 EET+0200 2024-02-28 20:00:00 EET+0200               2.782

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-01 00:00:00 EET+0200 2024-03-01 01:00:00 EET+0200              -0.002
	          2 2024-02-29 23:00:00 EET+0200 2024-03-01 01:00:00 EET+0200              -0.001
	          3 2024-02-29 22:00:00 EET+0200 2024-03-01 01:00:00 EET+0200            0.012667
	          4 2024-02-29 21:00:00 EET+0200 2024-03-01 01:00:00 EET+0200             0.09825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
