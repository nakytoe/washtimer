
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-02 08:00:00 EET+0200 2024-01-02 09:00:00 EET+0200              59.902
	          2 2024-01-02 08:00:00 EET+0200 2024-01-02 10:00:00 EET+0200             48.5555
	          3 2024-01-02 07:00:00 EET+0200 2024-01-02 10:00:00 EET+0200              42.704
	          4 2024-01-02 07:00:00 EET+0200 2024-01-02 11:00:00 EET+0200            39.77825

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-01-02 00:00:00 EET+0200 2024-01-02 01:00:00 EET+0200               5.455
	          2 2024-01-02 02:00:00 EET+0200 2024-01-02 04:00:00 EET+0200              6.0265
	          3 2024-01-02 00:00:00 EET+0200 2024-01-02 03:00:00 EET+0200            6.176667
	          4 2024-01-02 00:00:00 EET+0200 2024-01-02 04:00:00 EET+0200              6.0975


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
