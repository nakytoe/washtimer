
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-10 20:00:00 EEST+0300 2024-05-10 21:00:00 EEST+0300               3.138
	          2 2024-05-10 20:00:00 EEST+0300 2024-05-10 22:00:00 EEST+0300               3.138
	          3 2024-05-10 20:00:00 EEST+0300 2024-05-10 23:00:00 EEST+0300            3.116667
	          4 2024-05-10 20:00:00 EEST+0300 2024-05-11 00:00:00 EEST+0300             2.87225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-10 05:00:00 EEST+0300 2024-05-10 06:00:00 EEST+0300              -0.059
	          2 2024-05-10 04:00:00 EEST+0300 2024-05-10 06:00:00 EEST+0300             -0.0375
	          3 2024-05-10 04:00:00 EEST+0300 2024-05-10 07:00:00 EEST+0300           -0.030333
	          4 2024-05-10 03:00:00 EEST+0300 2024-05-10 07:00:00 EEST+0300            -0.02425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
