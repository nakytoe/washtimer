
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-10 11:00:00 EET+0200 2024-03-10 12:00:00 EET+0200              10.823
	          2 2024-03-10 10:00:00 EET+0200 2024-03-10 12:00:00 EET+0200             10.0615
	          3 2024-03-10 10:00:00 EET+0200 2024-03-10 13:00:00 EET+0200            9.807667
	          4 2024-03-10 09:00:00 EET+0200 2024-03-10 13:00:00 EET+0200             9.60275

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-11 00:00:00 EET+0200 2024-03-11 01:00:00 EET+0200               6.087
	          2 2024-03-10 23:00:00 EET+0200 2024-03-11 01:00:00 EET+0200               6.144
	          3 2024-03-10 22:00:00 EET+0200 2024-03-11 01:00:00 EET+0200               6.264
	          4 2024-03-10 21:00:00 EET+0200 2024-03-11 01:00:00 EET+0200             6.24825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
