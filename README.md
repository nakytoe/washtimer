
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-01 15:00:00 EET+0200 2024-03-01 16:00:00 EET+0200               3.677
	          2 2024-03-01 19:00:00 EET+0200 2024-03-01 21:00:00 EET+0200              3.6305
	          3 2024-03-01 18:00:00 EET+0200 2024-03-01 21:00:00 EET+0200            3.524333
	          4 2024-03-01 18:00:00 EET+0200 2024-03-01 22:00:00 EET+0200             3.46725

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-02 00:00:00 EET+0200 2024-03-02 01:00:00 EET+0200               3.218
	          2 2024-03-01 17:00:00 EET+0200 2024-03-01 19:00:00 EET+0200              3.2675
	          3 2024-03-01 22:00:00 EET+0200 2024-03-02 01:00:00 EET+0200            3.270333
	          4 2024-03-01 21:00:00 EET+0200 2024-03-02 01:00:00 EET+0200             3.27675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
