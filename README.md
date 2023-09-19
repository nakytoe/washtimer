
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-20 20:00:00 EEST+0300 2023-09-20 21:00:00 EEST+0300               1.308
	          2 2023-09-20 19:00:00 EEST+0300 2023-09-20 21:00:00 EEST+0300               1.272
	          3 2023-09-20 19:00:00 EEST+0300 2023-09-20 22:00:00 EEST+0300            1.227333
	          4 2023-09-20 18:00:00 EEST+0300 2023-09-20 22:00:00 EEST+0300               1.197

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-20 02:00:00 EEST+0300 2023-09-20 03:00:00 EEST+0300               -0.37
	          2 2023-09-20 02:00:00 EEST+0300 2023-09-20 04:00:00 EEST+0300               -0.37
	          3 2023-09-20 01:00:00 EEST+0300 2023-09-20 04:00:00 EEST+0300              -0.361
	          4 2023-09-20 01:00:00 EEST+0300 2023-09-20 05:00:00 EEST+0300            -0.35575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
