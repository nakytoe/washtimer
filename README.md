
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-29 10:00:00 EEST+0300 2023-09-29 11:00:00 EEST+0300                0.87
	          2 2023-09-29 10:00:00 EEST+0300 2023-09-29 12:00:00 EEST+0300               0.866
	          3 2023-09-29 10:00:00 EEST+0300 2023-09-29 13:00:00 EEST+0300                0.86
	          4 2023-09-29 09:00:00 EEST+0300 2023-09-29 13:00:00 EEST+0300             0.85025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-30 00:00:00 EEST+0300 2023-09-30 01:00:00 EEST+0300                0.02
	          2 2023-09-29 23:00:00 EEST+0300 2023-09-30 01:00:00 EEST+0300               0.116
	          3 2023-09-29 22:00:00 EEST+0300 2023-09-30 01:00:00 EEST+0300               0.186
	          4 2023-09-29 21:00:00 EEST+0300 2023-09-30 01:00:00 EEST+0300             0.25225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
