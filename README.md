
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-28 10:00:00 EET+0200 2024-03-28 11:00:00 EET+0200               6.886
	          2 2024-03-28 09:00:00 EET+0200 2024-03-28 11:00:00 EET+0200               6.758
	          3 2024-03-28 08:00:00 EET+0200 2024-03-28 11:00:00 EET+0200            6.487667
	          4 2024-03-28 08:00:00 EET+0200 2024-03-28 12:00:00 EET+0200             6.29675

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-29 00:00:00 EET+0200 2024-03-29 01:00:00 EET+0200               2.986
	          2 2024-03-28 15:00:00 EET+0200 2024-03-28 17:00:00 EET+0200              3.3565
	          3 2024-03-28 14:00:00 EET+0200 2024-03-28 17:00:00 EET+0200            3.489667
	          4 2024-03-28 13:00:00 EET+0200 2024-03-28 17:00:00 EET+0200              3.6375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
