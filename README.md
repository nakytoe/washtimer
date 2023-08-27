
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-27 20:00:00 EEST+0300 2023-08-27 21:00:00 EEST+0300              15.628
	          2 2023-08-27 19:00:00 EEST+0300 2023-08-27 21:00:00 EEST+0300              15.504
	          3 2023-08-27 20:00:00 EEST+0300 2023-08-27 23:00:00 EEST+0300              15.384
	          4 2023-08-27 19:00:00 EEST+0300 2023-08-27 23:00:00 EEST+0300              15.383

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-28 00:00:00 EEST+0300 2023-08-28 01:00:00 EEST+0300               2.887
	          2 2023-08-27 23:00:00 EEST+0300 2023-08-28 01:00:00 EEST+0300               3.924
	          3 2023-08-27 07:00:00 EEST+0300 2023-08-27 10:00:00 EEST+0300            7.216667
	          4 2023-08-27 07:00:00 EEST+0300 2023-08-27 11:00:00 EEST+0300               8.355


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
