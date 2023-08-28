
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-28 09:00:00 EEST+0300 2023-08-28 10:00:00 EEST+0300                21.7
	          2 2023-08-28 09:00:00 EEST+0300 2023-08-28 11:00:00 EEST+0300                21.7
	          3 2023-08-28 09:00:00 EEST+0300 2023-08-28 12:00:00 EEST+0300                21.7
	          4 2023-08-28 10:00:00 EEST+0300 2023-08-28 14:00:00 EEST+0300            20.91625

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-29 00:00:00 EEST+0300 2023-08-29 01:00:00 EEST+0300               3.416
	          2 2023-08-28 23:00:00 EEST+0300 2023-08-29 01:00:00 EEST+0300              4.1845
	          3 2023-08-28 22:00:00 EEST+0300 2023-08-29 01:00:00 EEST+0300            8.534333
	          4 2023-08-28 21:00:00 EEST+0300 2023-08-29 01:00:00 EEST+0300             11.5695


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
