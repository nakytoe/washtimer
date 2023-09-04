
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-04 11:00:00 EEST+0300 2023-09-04 12:00:00 EEST+0300              11.241
	          2 2023-09-04 11:00:00 EEST+0300 2023-09-04 13:00:00 EEST+0300               8.581
	          3 2023-09-04 10:00:00 EEST+0300 2023-09-04 13:00:00 EEST+0300            6.824667
	          4 2023-09-04 11:00:00 EEST+0300 2023-09-04 15:00:00 EEST+0300              5.9225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-05 00:00:00 EEST+0300 2023-09-05 01:00:00 EEST+0300               -0.21
	          2 2023-09-04 23:00:00 EEST+0300 2023-09-05 01:00:00 EEST+0300              -0.182
	          3 2023-09-04 22:00:00 EEST+0300 2023-09-05 01:00:00 EEST+0300              -0.124
	          4 2023-09-04 21:00:00 EEST+0300 2023-09-05 01:00:00 EEST+0300              -0.093


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
