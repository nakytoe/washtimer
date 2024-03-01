
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-01 13:00:00 EET+0200 2024-03-01 14:00:00 EET+0200               3.842
	          2 2024-03-01 13:00:00 EET+0200 2024-03-01 15:00:00 EET+0200               3.841
	          3 2024-03-01 12:00:00 EET+0200 2024-03-01 15:00:00 EET+0200            3.800667
	          4 2024-03-01 11:00:00 EET+0200 2024-03-01 15:00:00 EET+0200             3.77375

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-01 06:00:00 EET+0200 2024-03-01 07:00:00 EET+0200               2.537
	          2 2024-03-01 06:00:00 EET+0200 2024-03-01 08:00:00 EET+0200              2.6945
	          3 2024-03-01 06:00:00 EET+0200 2024-03-01 09:00:00 EET+0200            2.869667
	          4 2024-03-01 06:00:00 EET+0200 2024-03-01 10:00:00 EET+0200                3.02


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
