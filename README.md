
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-23 19:00:00 EEST+0300 2024-06-23 20:00:00 EEST+0300               4.567
	          2 2024-06-23 19:00:00 EEST+0300 2024-06-23 21:00:00 EEST+0300              4.5485
	          3 2024-06-23 19:00:00 EEST+0300 2024-06-23 22:00:00 EEST+0300               4.456
	          4 2024-06-23 19:00:00 EEST+0300 2024-06-23 23:00:00 EEST+0300             4.33125

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-23 15:00:00 EEST+0300 2024-06-23 16:00:00 EEST+0300               0.011
	          2 2024-06-23 14:00:00 EEST+0300 2024-06-23 16:00:00 EEST+0300               0.033
	          3 2024-06-23 13:00:00 EEST+0300 2024-06-23 16:00:00 EEST+0300            0.070667
	          4 2024-06-23 12:00:00 EEST+0300 2024-06-23 16:00:00 EEST+0300              0.1025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
