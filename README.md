
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-15 20:00:00 EEST+0300 2023-08-15 21:00:00 EEST+0300              15.338
	          2 2023-08-15 19:00:00 EEST+0300 2023-08-15 21:00:00 EEST+0300             14.3515
	          3 2023-08-15 18:00:00 EEST+0300 2023-08-15 21:00:00 EEST+0300           13.503333
	          4 2023-08-15 18:00:00 EEST+0300 2023-08-15 22:00:00 EEST+0300              10.891

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-16 00:00:00 EEST+0300 2023-08-16 01:00:00 EEST+0300               2.177
	          2 2023-08-15 23:00:00 EEST+0300 2023-08-16 01:00:00 EEST+0300               2.266
	          3 2023-08-15 22:00:00 EEST+0300 2023-08-16 01:00:00 EEST+0300            2.468333
	          4 2023-08-15 21:00:00 EEST+0300 2023-08-16 01:00:00 EEST+0300             2.61475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
