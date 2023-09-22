
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-22 10:00:00 EEST+0300 2023-09-22 11:00:00 EEST+0300               0.487
	          2 2023-09-22 10:00:00 EEST+0300 2023-09-22 12:00:00 EEST+0300               0.461
	          3 2023-09-22 09:00:00 EEST+0300 2023-09-22 12:00:00 EEST+0300               0.433
	          4 2023-09-22 09:00:00 EEST+0300 2023-09-22 13:00:00 EEST+0300               0.395

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-23 00:00:00 EEST+0300 2023-09-23 01:00:00 EEST+0300              -0.022
	          2 2023-09-22 23:00:00 EEST+0300 2023-09-23 01:00:00 EEST+0300              -0.011
	          3 2023-09-22 22:00:00 EEST+0300 2023-09-23 01:00:00 EEST+0300              -0.005
	          4 2023-09-22 21:00:00 EEST+0300 2023-09-23 01:00:00 EEST+0300             0.01425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
