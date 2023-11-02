
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-02 09:00:00 EET+0200 2023-11-02 10:00:00 EET+0200                9.41
	          2 2023-11-02 09:00:00 EET+0200 2023-11-02 11:00:00 EET+0200               8.993
	          3 2023-11-02 08:00:00 EET+0200 2023-11-02 11:00:00 EET+0200            8.813333
	          4 2023-11-02 08:00:00 EET+0200 2023-11-02 12:00:00 EET+0200              8.4725

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2023-11-03 00:00:00 EET+0200 2023-11-03 01:00:00 EET+0200               2.399
	          2 2023-11-02 23:00:00 EET+0200 2023-11-03 01:00:00 EET+0200               3.059
	          3 2023-11-02 22:00:00 EET+0200 2023-11-03 01:00:00 EET+0200            3.403667
	          4 2023-11-02 21:00:00 EET+0200 2023-11-03 01:00:00 EET+0200               3.531


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
