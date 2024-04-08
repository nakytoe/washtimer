
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-08 20:00:00 EEST+0300 2024-04-08 21:00:00 EEST+0300               6.551
	          2 2024-04-08 20:00:00 EEST+0300 2024-04-08 22:00:00 EEST+0300              6.5275
	          3 2024-04-08 20:00:00 EEST+0300 2024-04-08 23:00:00 EEST+0300            6.527333
	          4 2024-04-08 19:00:00 EEST+0300 2024-04-08 23:00:00 EEST+0300             6.49675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-08 14:00:00 EEST+0300 2024-04-08 15:00:00 EEST+0300               4.416
	          2 2024-04-08 14:00:00 EEST+0300 2024-04-08 16:00:00 EEST+0300               4.526
	          3 2024-04-08 13:00:00 EEST+0300 2024-04-08 16:00:00 EEST+0300               4.628
	          4 2024-04-08 12:00:00 EEST+0300 2024-04-08 16:00:00 EEST+0300             4.71075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
