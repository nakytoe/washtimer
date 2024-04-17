
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-18 08:00:00 EEST+0300 2024-04-18 09:00:00 EEST+0300              19.319
	          2 2024-04-18 08:00:00 EEST+0300 2024-04-18 10:00:00 EEST+0300             17.7935
	          3 2024-04-18 07:00:00 EEST+0300 2024-04-18 10:00:00 EEST+0300                16.9
	          4 2024-04-18 07:00:00 EEST+0300 2024-04-18 11:00:00 EEST+0300            15.80975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-17 16:00:00 EEST+0300 2024-04-17 17:00:00 EEST+0300               7.357
	          2 2024-04-17 23:00:00 EEST+0300 2024-04-18 01:00:00 EEST+0300               7.422
	          3 2024-04-17 23:00:00 EEST+0300 2024-04-18 02:00:00 EEST+0300            7.503333
	          4 2024-04-17 23:00:00 EEST+0300 2024-04-18 03:00:00 EEST+0300             7.56325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
