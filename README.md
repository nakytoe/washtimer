
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
	          1 2023-09-22 02:00:00 EEST+0300 2023-09-22 03:00:00 EEST+0300              -0.165
	          2 2023-09-22 01:00:00 EEST+0300 2023-09-22 03:00:00 EEST+0300              -0.161
	          3 2023-09-22 01:00:00 EEST+0300 2023-09-22 04:00:00 EEST+0300           -0.156333
	          4 2023-09-22 01:00:00 EEST+0300 2023-09-22 05:00:00 EEST+0300             -0.1465


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
