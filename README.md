
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-30 21:00:00 EEST+0300 2024-04-30 22:00:00 EEST+0300              16.366
	          2 2024-04-30 20:00:00 EEST+0300 2024-04-30 22:00:00 EEST+0300              15.745
	          3 2024-04-30 20:00:00 EEST+0300 2024-04-30 23:00:00 EEST+0300              14.149
	          4 2024-04-30 19:00:00 EEST+0300 2024-04-30 23:00:00 EEST+0300              13.284

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-01 15:00:00 EEST+0300 2024-05-01 16:00:00 EEST+0300               1.068
	          2 2024-05-01 14:00:00 EEST+0300 2024-05-01 16:00:00 EEST+0300               1.154
	          3 2024-05-01 14:00:00 EEST+0300 2024-05-01 17:00:00 EEST+0300            1.389667
	          4 2024-05-01 13:00:00 EEST+0300 2024-05-01 17:00:00 EEST+0300             1.56775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
