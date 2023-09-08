
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-08 20:00:00 EEST+0300 2023-09-08 21:00:00 EEST+0300               27.73
	          2 2023-09-08 08:00:00 EEST+0300 2023-09-08 10:00:00 EEST+0300             26.8185
	          3 2023-09-08 19:00:00 EEST+0300 2023-09-08 22:00:00 EEST+0300              24.269
	          4 2023-09-08 18:00:00 EEST+0300 2023-09-08 22:00:00 EEST+0300            21.54675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-09 00:00:00 EEST+0300 2023-09-09 01:00:00 EEST+0300               1.207
	          2 2023-09-08 23:00:00 EEST+0300 2023-09-09 01:00:00 EEST+0300              1.3325
	          3 2023-09-08 22:00:00 EEST+0300 2023-09-09 01:00:00 EEST+0300            1.944333
	          4 2023-09-08 21:00:00 EEST+0300 2023-09-09 01:00:00 EEST+0300               7.463


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
