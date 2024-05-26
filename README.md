
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-26 20:00:00 EEST+0300 2024-05-26 21:00:00 EEST+0300               1.561
	          2 2024-05-26 19:00:00 EEST+0300 2024-05-26 21:00:00 EEST+0300              1.5305
	          3 2024-05-26 18:00:00 EEST+0300 2024-05-26 21:00:00 EEST+0300            1.393667
	          4 2024-05-26 18:00:00 EEST+0300 2024-05-26 22:00:00 EEST+0300             1.28275

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-26 16:00:00 EEST+0300 2024-05-26 17:00:00 EEST+0300              -0.279
	          2 2024-05-27 02:00:00 EEST+0300 2024-05-27 04:00:00 EEST+0300              -0.176
	          3 2024-05-27 01:00:00 EEST+0300 2024-05-27 04:00:00 EEST+0300              -0.175
	          4 2024-05-27 01:00:00 EEST+0300 2024-05-27 05:00:00 EEST+0300            -0.17025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
