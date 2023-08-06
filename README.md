
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-06 11:00:00 EEST+0300 2023-08-06 12:00:00 EEST+0300                2.07
	          2 2023-08-06 11:00:00 EEST+0300 2023-08-06 13:00:00 EEST+0300               2.051
	          3 2023-08-06 10:00:00 EEST+0300 2023-08-06 13:00:00 EEST+0300               2.041
	          4 2023-08-06 10:00:00 EEST+0300 2023-08-06 14:00:00 EEST+0300             2.03425

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-07 00:00:00 EEST+0300 2023-08-07 01:00:00 EEST+0300                -0.1
	          2 2023-08-06 23:00:00 EEST+0300 2023-08-07 01:00:00 EEST+0300                0.03
	          3 2023-08-06 22:00:00 EEST+0300 2023-08-07 01:00:00 EEST+0300               0.159
	          4 2023-08-06 21:00:00 EEST+0300 2023-08-07 01:00:00 EEST+0300             0.26275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
