
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-05 20:00:00 EEST+0300 2023-08-05 21:00:00 EEST+0300               2.316
	          2 2023-08-05 19:00:00 EEST+0300 2023-08-05 21:00:00 EEST+0300               2.302
	          3 2023-08-05 19:00:00 EEST+0300 2023-08-05 22:00:00 EEST+0300               2.285
	          4 2023-08-05 19:00:00 EEST+0300 2023-08-05 23:00:00 EEST+0300             2.27275

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-05 07:00:00 EEST+0300 2023-08-05 08:00:00 EEST+0300               1.586
	          2 2023-08-05 07:00:00 EEST+0300 2023-08-05 09:00:00 EEST+0300              1.7315
	          3 2023-08-05 07:00:00 EEST+0300 2023-08-05 10:00:00 EEST+0300               1.821
	          4 2023-08-05 07:00:00 EEST+0300 2023-08-05 11:00:00 EEST+0300              1.8905


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
