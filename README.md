
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-16 20:00:00 EEST+0300 2024-05-16 21:00:00 EEST+0300                18.6
	          2 2024-05-16 19:00:00 EEST+0300 2024-05-16 21:00:00 EEST+0300              17.363
	          3 2024-05-16 19:00:00 EEST+0300 2024-05-16 22:00:00 EEST+0300           15.373333
	          4 2024-05-16 19:00:00 EEST+0300 2024-05-16 23:00:00 EEST+0300              15.079

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-15 16:00:00 EEST+0300 2024-05-15 17:00:00 EEST+0300              -0.009
	          2 2024-05-15 16:00:00 EEST+0300 2024-05-15 18:00:00 EEST+0300               0.103
	          3 2024-05-16 01:00:00 EEST+0300 2024-05-16 04:00:00 EEST+0300            0.314333
	          4 2024-05-16 01:00:00 EEST+0300 2024-05-16 05:00:00 EEST+0300              0.3755


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
