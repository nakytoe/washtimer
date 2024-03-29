
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-29 18:00:00 EET+0200 2024-03-29 19:00:00 EET+0200               5.248
	          2 2024-03-29 18:00:00 EET+0200 2024-03-29 20:00:00 EET+0200               5.225
	          3 2024-03-29 18:00:00 EET+0200 2024-03-29 21:00:00 EET+0200            5.214333
	          4 2024-03-29 18:00:00 EET+0200 2024-03-29 22:00:00 EET+0200             5.21225

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-29 14:00:00 EET+0200 2024-03-29 15:00:00 EET+0200               1.223
	          2 2024-03-29 13:00:00 EET+0200 2024-03-29 15:00:00 EET+0200              1.4175
	          3 2024-03-29 13:00:00 EET+0200 2024-03-29 16:00:00 EET+0200            1.500667
	          4 2024-03-29 12:00:00 EET+0200 2024-03-29 16:00:00 EET+0200             1.70925


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
