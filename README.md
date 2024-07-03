
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-03 16:00:00 EEST+0300 2024-07-03 17:00:00 EEST+0300               4.598
	          2 2024-07-03 16:00:00 EEST+0300 2024-07-03 18:00:00 EEST+0300              4.5745
	          3 2024-07-03 16:00:00 EEST+0300 2024-07-03 19:00:00 EEST+0300            4.537333
	          4 2024-07-03 16:00:00 EEST+0300 2024-07-03 20:00:00 EEST+0300             4.54075

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-04 17:00:00 EEST+0300 2024-07-04 18:00:00 EEST+0300              -0.001
	          2 2024-07-04 16:00:00 EEST+0300 2024-07-04 18:00:00 EEST+0300             -0.0005
	          3 2024-07-04 15:00:00 EEST+0300 2024-07-04 18:00:00 EEST+0300           -0.000333
	          4 2024-07-04 14:00:00 EEST+0300 2024-07-04 18:00:00 EEST+0300             0.02975


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
