
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-27 09:00:00 EEST+0300 2023-09-27 10:00:00 EEST+0300              15.493
	          2 2023-09-27 09:00:00 EEST+0300 2023-09-27 11:00:00 EEST+0300             11.3395
	          3 2023-09-27 08:00:00 EEST+0300 2023-09-27 11:00:00 EEST+0300               7.958
	          4 2023-09-27 08:00:00 EEST+0300 2023-09-27 12:00:00 EEST+0300              6.1825

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-28 00:00:00 EEST+0300 2023-09-28 01:00:00 EEST+0300               0.254
	          2 2023-09-27 23:00:00 EEST+0300 2023-09-28 01:00:00 EEST+0300              0.2685
	          3 2023-09-27 22:00:00 EEST+0300 2023-09-28 01:00:00 EEST+0300               0.301
	          4 2023-09-27 21:00:00 EEST+0300 2023-09-28 01:00:00 EEST+0300               0.332


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
