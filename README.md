
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-27 20:00:00 EEST+0300 2024-04-27 21:00:00 EEST+0300              14.868
	          2 2024-04-27 20:00:00 EEST+0300 2024-04-27 22:00:00 EEST+0300             14.3945
	          3 2024-04-27 19:00:00 EEST+0300 2024-04-27 22:00:00 EEST+0300              13.151
	          4 2024-04-27 19:00:00 EEST+0300 2024-04-27 23:00:00 EEST+0300            12.49825

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-27 14:00:00 EEST+0300 2024-04-27 15:00:00 EEST+0300               5.287
	          2 2024-04-27 14:00:00 EEST+0300 2024-04-27 16:00:00 EEST+0300              5.3125
	          3 2024-04-27 13:00:00 EEST+0300 2024-04-27 16:00:00 EEST+0300            5.336333
	          4 2024-04-27 12:00:00 EEST+0300 2024-04-27 16:00:00 EEST+0300              5.3665


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
