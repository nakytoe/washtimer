
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-23 19:00:00 EEST+0300 2024-06-23 20:00:00 EEST+0300               4.567
	          2 2024-06-23 19:00:00 EEST+0300 2024-06-23 21:00:00 EEST+0300              4.5485
	          3 2024-06-22 19:00:00 EEST+0300 2024-06-22 22:00:00 EEST+0300            4.480667
	          4 2024-06-22 18:00:00 EEST+0300 2024-06-22 22:00:00 EEST+0300               4.448

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-23 03:00:00 EEST+0300 2024-06-23 04:00:00 EEST+0300              -0.002
	          2 2024-06-23 02:00:00 EEST+0300 2024-06-23 04:00:00 EEST+0300             -0.0015
	          3 2024-06-23 01:00:00 EEST+0300 2024-06-23 04:00:00 EEST+0300              -0.001
	          4 2024-06-23 01:00:00 EEST+0300 2024-06-23 05:00:00 EEST+0300            -0.00075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
