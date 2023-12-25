
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-25 18:00:00 EET+0200 2023-12-25 19:00:00 EET+0200               4.809
	          2 2023-12-25 18:00:00 EET+0200 2023-12-25 20:00:00 EET+0200              4.7615
	          3 2023-12-25 18:00:00 EET+0200 2023-12-25 21:00:00 EET+0200            4.624333
	          4 2023-12-25 17:00:00 EET+0200 2023-12-25 21:00:00 EET+0200               4.553

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-25 07:00:00 EET+0200 2023-12-25 08:00:00 EET+0200               2.568
	          2 2023-12-25 06:00:00 EET+0200 2023-12-25 08:00:00 EET+0200               2.656
	          3 2023-12-25 06:00:00 EET+0200 2023-12-25 09:00:00 EET+0200            2.922333
	          4 2023-12-25 06:00:00 EET+0200 2023-12-25 10:00:00 EET+0200             3.13875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
