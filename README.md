
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-15 19:00:00 EET+0200 2024-03-15 20:00:00 EET+0200               7.042
	          2 2024-03-15 18:00:00 EET+0200 2024-03-15 20:00:00 EET+0200               6.969
	          3 2024-03-15 18:00:00 EET+0200 2024-03-15 21:00:00 EET+0200            6.803667
	          4 2024-03-15 17:00:00 EET+0200 2024-03-15 21:00:00 EET+0200                6.71

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-15 06:00:00 EET+0200 2024-03-15 07:00:00 EET+0200               1.662
	          2 2024-03-15 06:00:00 EET+0200 2024-03-15 08:00:00 EET+0200              2.5205
	          3 2024-03-15 06:00:00 EET+0200 2024-03-15 09:00:00 EET+0200            3.142333
	          4 2024-03-15 06:00:00 EET+0200 2024-03-15 10:00:00 EET+0200              3.5815


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
