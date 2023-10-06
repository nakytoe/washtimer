
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-06 19:00:00 EEST+0300 2023-10-06 20:00:00 EEST+0300               0.502
	          2 2023-10-06 18:00:00 EEST+0300 2023-10-06 20:00:00 EEST+0300              0.4725
	          3 2023-10-06 17:00:00 EEST+0300 2023-10-06 20:00:00 EEST+0300            0.456667
	          4 2023-10-06 16:00:00 EEST+0300 2023-10-06 20:00:00 EEST+0300               0.437

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-07 04:00:00 EEST+0300 2023-10-07 05:00:00 EEST+0300              -0.431
	          2 2023-10-07 03:00:00 EEST+0300 2023-10-07 05:00:00 EEST+0300              -0.397
	          3 2023-10-07 04:00:00 EEST+0300 2023-10-07 07:00:00 EEST+0300              -0.386
	          4 2023-10-07 03:00:00 EEST+0300 2023-10-07 07:00:00 EEST+0300            -0.38025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
