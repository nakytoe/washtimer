
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-29 22:00:00 EEST+0300 2024-06-29 23:00:00 EEST+0300               0.186
	          2 2024-06-29 22:00:00 EEST+0300 2024-06-30 00:00:00 EEST+0300              0.0935
	          3 2024-06-29 21:00:00 EEST+0300 2024-06-30 00:00:00 EEST+0300            0.062333
	          4 2024-06-29 20:00:00 EEST+0300 2024-06-30 00:00:00 EEST+0300             0.04675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-29 15:00:00 EEST+0300 2024-06-29 16:00:00 EEST+0300              -0.242
	          2 2024-06-29 15:00:00 EEST+0300 2024-06-29 17:00:00 EEST+0300             -0.2355
	          3 2024-06-29 14:00:00 EEST+0300 2024-06-29 17:00:00 EEST+0300           -0.226667
	          4 2024-06-29 12:00:00 EEST+0300 2024-06-29 16:00:00 EEST+0300            -0.22025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
