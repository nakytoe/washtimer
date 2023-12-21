
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-21 20:00:00 EET+0200 2023-12-21 21:00:00 EET+0200                5.84
	          2 2023-12-21 20:00:00 EET+0200 2023-12-21 22:00:00 EET+0200                5.46
	          3 2023-12-21 19:00:00 EET+0200 2023-12-21 22:00:00 EET+0200            5.230667
	          4 2023-12-21 18:00:00 EET+0200 2023-12-21 22:00:00 EET+0200             5.03725

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-22 04:00:00 EET+0200 2023-12-22 05:00:00 EET+0200               0.501
	          2 2023-12-22 03:00:00 EET+0200 2023-12-22 05:00:00 EET+0200              0.5555
	          3 2023-12-22 03:00:00 EET+0200 2023-12-22 06:00:00 EET+0200               0.606
	          4 2023-12-22 02:00:00 EET+0200 2023-12-22 06:00:00 EET+0200               0.783


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
