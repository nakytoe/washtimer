
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-06 17:00:00 EEST+0300 2023-08-06 18:00:00 EEST+0300               1.464
	          2 2023-08-06 17:00:00 EEST+0300 2023-08-06 19:00:00 EEST+0300                1.46
	          3 2023-08-06 17:00:00 EEST+0300 2023-08-06 20:00:00 EEST+0300            1.428667
	          4 2023-08-06 17:00:00 EEST+0300 2023-08-06 21:00:00 EEST+0300             1.36375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-07 04:00:00 EEST+0300 2023-08-07 05:00:00 EEST+0300              -0.254
	          2 2023-08-07 04:00:00 EEST+0300 2023-08-07 06:00:00 EEST+0300              -0.246
	          3 2023-08-07 03:00:00 EEST+0300 2023-08-07 06:00:00 EEST+0300              -0.233
	          4 2023-08-07 03:00:00 EEST+0300 2023-08-07 07:00:00 EEST+0300            -0.21675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
