
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-02 19:00:00 EET+0200 2024-03-02 20:00:00 EET+0200               7.927
	          2 2024-03-02 18:00:00 EET+0200 2024-03-02 20:00:00 EET+0200               7.874
	          3 2024-03-02 18:00:00 EET+0200 2024-03-02 21:00:00 EET+0200            7.746667
	          4 2024-03-02 17:00:00 EET+0200 2024-03-02 21:00:00 EET+0200               7.645

The min prices for today:

	program [h]                   start time                     end time mean price [€c/kWh]
	          1 2024-03-02 07:00:00 EET+0200 2024-03-02 08:00:00 EET+0200                4.52
	          2 2024-03-02 07:00:00 EET+0200 2024-03-02 09:00:00 EET+0200               4.609
	          3 2024-03-02 06:00:00 EET+0200 2024-03-02 09:00:00 EET+0200            4.641333
	          4 2024-03-02 06:00:00 EET+0200 2024-03-02 10:00:00 EET+0200             4.71875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
