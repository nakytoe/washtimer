
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-11 19:00:00 EEST+0300 2024-04-11 20:00:00 EEST+0300               3.174
	          2 2024-04-11 19:00:00 EEST+0300 2024-04-11 21:00:00 EEST+0300               3.161
	          3 2024-04-11 18:00:00 EEST+0300 2024-04-11 21:00:00 EEST+0300            3.028667
	          4 2024-04-11 18:00:00 EEST+0300 2024-04-11 22:00:00 EEST+0300              2.9225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-11 00:00:00 EEST+0300 2024-04-11 01:00:00 EEST+0300              -0.309
	          2 2024-04-11 00:00:00 EEST+0300 2024-04-11 02:00:00 EEST+0300              -0.308
	          3 2024-04-11 00:00:00 EEST+0300 2024-04-11 03:00:00 EEST+0300           -0.307667
	          4 2024-04-11 00:00:00 EEST+0300 2024-04-11 04:00:00 EEST+0300            -0.30725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
