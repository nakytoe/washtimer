
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-16 11:00:00 EET+0200 2024-03-16 12:00:00 EET+0200                4.86
	          2 2024-03-16 10:00:00 EET+0200 2024-03-16 12:00:00 EET+0200               4.841
	          3 2024-03-16 10:00:00 EET+0200 2024-03-16 13:00:00 EET+0200            4.834667
	          4 2024-03-16 09:00:00 EET+0200 2024-03-16 13:00:00 EET+0200              4.7755

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-16 15:00:00 EET+0200 2024-03-16 16:00:00 EET+0200               1.611
	          2 2024-03-16 14:00:00 EET+0200 2024-03-16 16:00:00 EET+0200              2.1635
	          3 2024-03-16 14:00:00 EET+0200 2024-03-16 17:00:00 EET+0200               2.641
	          4 2024-03-16 14:00:00 EET+0200 2024-03-16 18:00:00 EET+0200              3.0415


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
