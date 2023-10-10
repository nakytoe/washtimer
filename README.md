
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-10 16:00:00 EEST+0300 2023-10-10 17:00:00 EEST+0300              15.401
	          2 2023-10-10 16:00:00 EEST+0300 2023-10-10 18:00:00 EEST+0300             10.8475
	          3 2023-10-10 16:00:00 EEST+0300 2023-10-10 19:00:00 EEST+0300               8.998
	          4 2023-10-10 16:00:00 EEST+0300 2023-10-10 20:00:00 EEST+0300             7.56625

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-11 04:00:00 EEST+0300 2023-10-11 05:00:00 EEST+0300              -0.515
	          2 2023-10-11 03:00:00 EEST+0300 2023-10-11 05:00:00 EEST+0300              -0.512
	          3 2023-10-11 02:00:00 EEST+0300 2023-10-11 05:00:00 EEST+0300           -0.507333
	          4 2023-10-11 02:00:00 EEST+0300 2023-10-11 06:00:00 EEST+0300              -0.502


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
