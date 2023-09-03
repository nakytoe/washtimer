
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-03 19:00:00 EEST+0300 2023-09-03 20:00:00 EEST+0300              13.546
	          2 2023-09-03 18:00:00 EEST+0300 2023-09-03 20:00:00 EEST+0300               12.59
	          3 2023-09-03 17:00:00 EEST+0300 2023-09-03 20:00:00 EEST+0300           10.611333
	          4 2023-09-03 17:00:00 EEST+0300 2023-09-03 21:00:00 EEST+0300              9.2915

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-04 00:00:00 EEST+0300 2023-09-04 01:00:00 EEST+0300               0.172
	          2 2023-09-03 23:00:00 EEST+0300 2023-09-04 01:00:00 EEST+0300               0.686
	          3 2023-09-03 22:00:00 EEST+0300 2023-09-04 01:00:00 EEST+0300               1.117
	          4 2023-09-03 21:00:00 EEST+0300 2023-09-04 01:00:00 EEST+0300               1.446


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
