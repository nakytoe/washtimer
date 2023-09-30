
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-30 19:00:00 EEST+0300 2023-09-30 20:00:00 EEST+0300                0.62
	          2 2023-09-30 19:00:00 EEST+0300 2023-09-30 21:00:00 EEST+0300              0.5785
	          3 2023-09-30 18:00:00 EEST+0300 2023-09-30 21:00:00 EEST+0300            0.515333
	          4 2023-09-30 17:00:00 EEST+0300 2023-09-30 21:00:00 EEST+0300             0.44475

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-01 00:00:00 EEST+0300 2023-10-01 01:00:00 EEST+0300                 0.0
	          2 2023-09-30 23:00:00 EEST+0300 2023-10-01 01:00:00 EEST+0300               0.034
	          3 2023-09-30 22:00:00 EEST+0300 2023-10-01 01:00:00 EEST+0300               0.076
	          4 2023-09-30 21:00:00 EEST+0300 2023-10-01 01:00:00 EEST+0300             0.10525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
