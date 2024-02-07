
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-07 07:00:00 EET+0200 2024-02-07 08:00:00 EET+0200              19.219
	          2 2024-02-07 07:00:00 EET+0200 2024-02-07 09:00:00 EET+0200              18.202
	          3 2024-02-07 07:00:00 EET+0200 2024-02-07 10:00:00 EET+0200              17.287
	          4 2024-02-07 16:00:00 EET+0200 2024-02-07 20:00:00 EET+0200              17.171

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-02-08 00:00:00 EET+0200 2024-02-08 01:00:00 EET+0200              11.795
	          2 2024-02-07 23:00:00 EET+0200 2024-02-08 01:00:00 EET+0200             11.8215
	          3 2024-02-07 22:00:00 EET+0200 2024-02-08 01:00:00 EET+0200              11.953
	          4 2024-02-07 21:00:00 EET+0200 2024-02-08 01:00:00 EET+0200              12.062


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
