
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-13 20:00:00 EEST+0300 2024-07-13 21:00:00 EEST+0300               3.257
	          2 2024-07-13 08:00:00 EEST+0300 2024-07-13 10:00:00 EEST+0300              3.1445
	          3 2024-07-13 08:00:00 EEST+0300 2024-07-13 11:00:00 EEST+0300               2.963
	          4 2024-07-13 07:00:00 EEST+0300 2024-07-13 11:00:00 EEST+0300               2.828

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-13 14:00:00 EEST+0300 2024-07-13 15:00:00 EEST+0300              -0.087
	          2 2024-07-13 14:00:00 EEST+0300 2024-07-13 16:00:00 EEST+0300              -0.084
	          3 2024-07-13 14:00:00 EEST+0300 2024-07-13 17:00:00 EEST+0300              -0.058
	          4 2024-07-13 13:00:00 EEST+0300 2024-07-13 17:00:00 EEST+0300            -0.04375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
