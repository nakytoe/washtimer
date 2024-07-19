
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-20 18:00:00 EEST+0300 2024-07-20 19:00:00 EEST+0300               3.131
	          2 2024-07-20 18:00:00 EEST+0300 2024-07-20 20:00:00 EEST+0300              3.1285
	          3 2024-07-20 18:00:00 EEST+0300 2024-07-20 21:00:00 EEST+0300            3.127667
	          4 2024-07-20 18:00:00 EEST+0300 2024-07-20 22:00:00 EEST+0300             3.10575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-20 14:00:00 EEST+0300 2024-07-20 15:00:00 EEST+0300               0.002
	          2 2024-07-20 14:00:00 EEST+0300 2024-07-20 16:00:00 EEST+0300              0.0285
	          3 2024-07-20 13:00:00 EEST+0300 2024-07-20 16:00:00 EEST+0300            0.075667
	          4 2024-07-20 12:00:00 EEST+0300 2024-07-20 16:00:00 EEST+0300              0.1735


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
