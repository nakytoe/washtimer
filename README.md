
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-04 20:00:00 EEST+0300 2024-06-04 21:00:00 EEST+0300              31.005
	          2 2024-06-04 20:00:00 EEST+0300 2024-06-04 22:00:00 EEST+0300                29.5
	          3 2024-06-04 19:00:00 EEST+0300 2024-06-04 22:00:00 EEST+0300           27.933667
	          4 2024-06-04 19:00:00 EEST+0300 2024-06-04 23:00:00 EEST+0300             27.1505

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-04 03:00:00 EEST+0300 2024-06-04 04:00:00 EEST+0300                0.17
	          2 2024-06-04 02:00:00 EEST+0300 2024-06-04 04:00:00 EEST+0300               0.199
	          3 2024-06-04 02:00:00 EEST+0300 2024-06-04 05:00:00 EEST+0300            0.211667
	          4 2024-06-04 02:00:00 EEST+0300 2024-06-04 06:00:00 EEST+0300               0.254


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
