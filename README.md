
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-26 18:00:00 EEST+0300 2023-09-26 19:00:00 EEST+0300               0.782
	          2 2023-09-26 17:00:00 EEST+0300 2023-09-26 19:00:00 EEST+0300               0.764
	          3 2023-09-26 16:00:00 EEST+0300 2023-09-26 19:00:00 EEST+0300            0.747333
	          4 2023-09-26 15:00:00 EEST+0300 2023-09-26 19:00:00 EEST+0300              0.7215

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-27 00:00:00 EEST+0300 2023-09-27 01:00:00 EEST+0300              -0.004
	          2 2023-09-26 23:00:00 EEST+0300 2023-09-27 01:00:00 EEST+0300              0.0245
	          3 2023-09-26 22:00:00 EEST+0300 2023-09-27 01:00:00 EEST+0300            0.084667
	          4 2023-09-26 21:00:00 EEST+0300 2023-09-27 01:00:00 EEST+0300                0.15


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
