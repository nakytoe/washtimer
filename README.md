
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-15 16:00:00 EEST+0300 2023-09-15 17:00:00 EEST+0300              10.616
	          2 2023-09-15 16:00:00 EEST+0300 2023-09-15 18:00:00 EEST+0300              7.2755
	          3 2023-09-15 16:00:00 EEST+0300 2023-09-15 19:00:00 EEST+0300            5.544333
	          4 2023-09-15 16:00:00 EEST+0300 2023-09-15 20:00:00 EEST+0300             4.64025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-16 00:00:00 EEST+0300 2023-09-16 01:00:00 EEST+0300               0.746
	          2 2023-09-15 23:00:00 EEST+0300 2023-09-16 01:00:00 EEST+0300              0.9265
	          3 2023-09-16 04:00:00 EEST+0300 2023-09-16 07:00:00 EEST+0300            0.977333
	          4 2023-09-16 03:00:00 EEST+0300 2023-09-16 07:00:00 EEST+0300             0.99675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
