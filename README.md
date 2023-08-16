
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-16 19:00:00 EEST+0300 2023-08-16 20:00:00 EEST+0300               3.507
	          2 2023-08-16 18:00:00 EEST+0300 2023-08-16 20:00:00 EEST+0300               3.365
	          3 2023-08-16 18:00:00 EEST+0300 2023-08-16 21:00:00 EEST+0300               3.065
	          4 2023-08-16 18:00:00 EEST+0300 2023-08-16 22:00:00 EEST+0300               2.947

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-17 00:00:00 EEST+0300 2023-08-17 01:00:00 EEST+0300               0.894
	          2 2023-08-16 23:00:00 EEST+0300 2023-08-17 01:00:00 EEST+0300              1.3055
	          3 2023-08-16 22:00:00 EEST+0300 2023-08-17 01:00:00 EEST+0300            1.572333
	          4 2023-08-16 21:00:00 EEST+0300 2023-08-17 01:00:00 EEST+0300              1.8275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
