
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-07 20:00:00 EEST+0300 2024-06-07 21:00:00 EEST+0300              23.566
	          2 2024-06-07 19:00:00 EEST+0300 2024-06-07 21:00:00 EEST+0300             19.7165
	          3 2024-06-07 18:00:00 EEST+0300 2024-06-07 21:00:00 EEST+0300           16.482667
	          4 2024-06-07 18:00:00 EEST+0300 2024-06-07 22:00:00 EEST+0300            13.88325

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-08 13:00:00 EEST+0300 2024-06-08 14:00:00 EEST+0300               0.383
	          2 2024-06-08 13:00:00 EEST+0300 2024-06-08 15:00:00 EEST+0300               0.416
	          3 2024-06-08 13:00:00 EEST+0300 2024-06-08 16:00:00 EEST+0300            0.405333
	          4 2024-06-08 12:00:00 EEST+0300 2024-06-08 16:00:00 EEST+0300             0.43075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
