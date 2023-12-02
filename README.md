
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-02 19:00:00 EET+0200 2023-12-02 20:00:00 EET+0200              17.975
	          2 2023-12-02 18:00:00 EET+0200 2023-12-02 20:00:00 EET+0200              17.918
	          3 2023-12-02 17:00:00 EET+0200 2023-12-02 20:00:00 EET+0200               17.31
	          4 2023-12-02 17:00:00 EET+0200 2023-12-02 21:00:00 EET+0200            16.99875

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-12-02 06:00:00 EET+0200 2023-12-02 07:00:00 EET+0200              11.869
	          2 2023-12-02 06:00:00 EET+0200 2023-12-02 08:00:00 EET+0200             11.9205
	          3 2023-12-02 06:00:00 EET+0200 2023-12-02 09:00:00 EET+0200           12.147667
	          4 2023-12-02 06:00:00 EET+0200 2023-12-02 10:00:00 EET+0200            12.72575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
