
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-28 10:00:00 EEST+0300 2023-09-28 11:00:00 EEST+0300              13.745
	          2 2023-09-28 10:00:00 EEST+0300 2023-09-28 12:00:00 EEST+0300              12.661
	          3 2023-09-28 10:00:00 EEST+0300 2023-09-28 13:00:00 EEST+0300              12.101
	          4 2023-09-28 10:00:00 EEST+0300 2023-09-28 14:00:00 EEST+0300            11.14075

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-29 00:00:00 EEST+0300 2023-09-29 01:00:00 EEST+0300              -0.065
	          2 2023-09-28 23:00:00 EEST+0300 2023-09-29 01:00:00 EEST+0300              -0.029
	          3 2023-09-28 22:00:00 EEST+0300 2023-09-29 01:00:00 EEST+0300                0.05
	          4 2023-09-28 21:00:00 EEST+0300 2023-09-29 01:00:00 EEST+0300              0.1225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
