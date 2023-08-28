
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-28 20:00:00 EEST+0300 2023-08-28 21:00:00 EEST+0300              21.695
	          2 2023-08-28 20:00:00 EEST+0300 2023-08-28 22:00:00 EEST+0300              21.185
	          3 2023-08-28 19:00:00 EEST+0300 2023-08-28 22:00:00 EEST+0300           20.854333
	          4 2023-08-28 18:00:00 EEST+0300 2023-08-28 22:00:00 EEST+0300             20.2925

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-29 03:00:00 EEST+0300 2023-08-29 04:00:00 EEST+0300               1.793
	          2 2023-08-29 03:00:00 EEST+0300 2023-08-29 05:00:00 EEST+0300              1.7975
	          3 2023-08-29 02:00:00 EEST+0300 2023-08-29 05:00:00 EEST+0300               1.822
	          4 2023-08-29 02:00:00 EEST+0300 2023-08-29 06:00:00 EEST+0300             1.83875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
