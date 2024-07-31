
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-01 15:00:00 EEST+0300 2024-08-01 16:00:00 EEST+0300               7.659
	          2 2024-08-01 14:00:00 EEST+0300 2024-08-01 16:00:00 EEST+0300               7.452
	          3 2024-08-01 14:00:00 EEST+0300 2024-08-01 17:00:00 EEST+0300            7.018667
	          4 2024-08-01 13:00:00 EEST+0300 2024-08-01 17:00:00 EEST+0300             6.78325

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-01 00:00:00 EEST+0300 2024-08-01 01:00:00 EEST+0300              -0.001
	          2 2024-08-01 03:00:00 EEST+0300 2024-08-01 05:00:00 EEST+0300              -0.001
	          3 2024-08-01 02:00:00 EEST+0300 2024-08-01 05:00:00 EEST+0300           -0.000667
	          4 2024-08-01 02:00:00 EEST+0300 2024-08-01 06:00:00 EEST+0300             -0.0005


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
