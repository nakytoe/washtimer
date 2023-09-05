
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-05 10:00:00 EEST+0300 2023-09-05 11:00:00 EEST+0300              16.223
	          2 2023-09-05 09:00:00 EEST+0300 2023-09-05 11:00:00 EEST+0300             14.9315
	          3 2023-09-05 09:00:00 EEST+0300 2023-09-05 12:00:00 EEST+0300           12.242667
	          4 2023-09-05 09:00:00 EEST+0300 2023-09-05 13:00:00 EEST+0300            10.47025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-06 00:00:00 EEST+0300 2023-09-06 01:00:00 EEST+0300              -0.016
	          2 2023-09-05 23:00:00 EEST+0300 2023-09-06 01:00:00 EEST+0300              -0.005
	          3 2023-09-05 22:00:00 EEST+0300 2023-09-06 01:00:00 EEST+0300               0.069
	          4 2023-09-05 21:00:00 EEST+0300 2023-09-06 01:00:00 EEST+0300             0.16275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
