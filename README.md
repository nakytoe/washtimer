
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-26 19:00:00 EET+0200 2024-02-26 20:00:00 EET+0200                8.06
	          2 2024-02-26 18:00:00 EET+0200 2024-02-26 20:00:00 EET+0200              7.7505
	          3 2024-02-26 18:00:00 EET+0200 2024-02-26 21:00:00 EET+0200            7.647333
	          4 2024-02-26 17:00:00 EET+0200 2024-02-26 21:00:00 EET+0200             7.58525

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-26 01:00:00 EET+0200 2024-02-26 02:00:00 EET+0200                3.29
	          2 2024-02-26 01:00:00 EET+0200 2024-02-26 03:00:00 EET+0200              3.3185
	          3 2024-02-26 01:00:00 EET+0200 2024-02-26 04:00:00 EET+0200            3.359667
	          4 2024-02-26 01:00:00 EET+0200 2024-02-26 05:00:00 EET+0200              3.4125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
