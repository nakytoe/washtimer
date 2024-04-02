
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-03 19:00:00 EEST+0300 2024-04-03 20:00:00 EEST+0300               7.356
	          2 2024-04-03 19:00:00 EEST+0300 2024-04-03 21:00:00 EEST+0300               7.236
	          3 2024-04-03 18:00:00 EEST+0300 2024-04-03 21:00:00 EEST+0300            7.178667
	          4 2024-04-03 19:00:00 EEST+0300 2024-04-03 23:00:00 EEST+0300               7.113

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-03 00:00:00 EEST+0300 2024-04-03 01:00:00 EEST+0300               0.206
	          2 2024-04-03 00:00:00 EEST+0300 2024-04-03 02:00:00 EEST+0300              1.6705
	          3 2024-04-03 00:00:00 EEST+0300 2024-04-03 03:00:00 EEST+0300            1.966333
	          4 2024-04-03 00:00:00 EEST+0300 2024-04-03 04:00:00 EEST+0300             2.00025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
