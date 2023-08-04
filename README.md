
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-04 19:00:00 EEST+0300 2023-08-04 20:00:00 EEST+0300                3.08
	          2 2023-08-04 19:00:00 EEST+0300 2023-08-04 21:00:00 EEST+0300               3.061
	          3 2023-08-04 18:00:00 EEST+0300 2023-08-04 21:00:00 EEST+0300               3.012
	          4 2023-08-04 18:00:00 EEST+0300 2023-08-04 22:00:00 EEST+0300             2.98075

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-05 04:00:00 EEST+0300 2023-08-05 05:00:00 EEST+0300               0.601
	          2 2023-08-05 03:00:00 EEST+0300 2023-08-05 05:00:00 EEST+0300              0.6035
	          3 2023-08-05 03:00:00 EEST+0300 2023-08-05 06:00:00 EEST+0300               0.606
	          4 2023-08-05 02:00:00 EEST+0300 2023-08-05 06:00:00 EEST+0300               0.668


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
