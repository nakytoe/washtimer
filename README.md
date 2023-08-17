
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-18 09:00:00 EEST+0300 2023-08-18 10:00:00 EEST+0300              33.536
	          2 2023-08-18 08:00:00 EEST+0300 2023-08-18 10:00:00 EEST+0300             29.6985
	          3 2023-08-18 08:00:00 EEST+0300 2023-08-18 11:00:00 EEST+0300           27.568333
	          4 2023-08-18 08:00:00 EEST+0300 2023-08-18 12:00:00 EEST+0300            25.26025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-19 00:00:00 EEST+0300 2023-08-19 01:00:00 EEST+0300               1.784
	          2 2023-08-18 23:00:00 EEST+0300 2023-08-19 01:00:00 EEST+0300                1.86
	          3 2023-08-18 03:00:00 EEST+0300 2023-08-18 06:00:00 EEST+0300               2.053
	          4 2023-08-18 02:00:00 EEST+0300 2023-08-18 06:00:00 EEST+0300              2.0845


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
