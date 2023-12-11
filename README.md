
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-12 08:00:00 EET+0200 2023-12-12 09:00:00 EET+0200              24.804
	          2 2023-12-12 08:00:00 EET+0200 2023-12-12 10:00:00 EET+0200              24.804
	          3 2023-12-12 08:00:00 EET+0200 2023-12-12 11:00:00 EET+0200              24.803
	          4 2023-12-12 08:00:00 EET+0200 2023-12-12 12:00:00 EET+0200            24.30625

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-12 00:00:00 EET+0200 2023-12-12 01:00:00 EET+0200              10.766
	          2 2023-12-11 23:00:00 EET+0200 2023-12-12 01:00:00 EET+0200             11.5035
	          3 2023-12-12 02:00:00 EET+0200 2023-12-12 05:00:00 EET+0200              11.729
	          4 2023-12-12 02:00:00 EET+0200 2023-12-12 06:00:00 EET+0200             11.7445


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
