
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-27 09:00:00 EEST+0300 2023-10-27 10:00:00 EEST+0300               18.55
	          2 2023-10-27 09:00:00 EEST+0300 2023-10-27 11:00:00 EEST+0300              18.449
	          3 2023-10-27 09:00:00 EEST+0300 2023-10-27 12:00:00 EEST+0300           16.782333
	          4 2023-10-27 09:00:00 EEST+0300 2023-10-27 13:00:00 EEST+0300            15.95075

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-27 00:00:00 EEST+0300 2023-10-27 01:00:00 EEST+0300               4.243
	          2 2023-10-26 23:00:00 EEST+0300 2023-10-27 01:00:00 EEST+0300              4.4585
	          3 2023-10-26 22:00:00 EEST+0300 2023-10-27 01:00:00 EEST+0300            4.601333
	          4 2023-10-26 21:00:00 EEST+0300 2023-10-27 01:00:00 EEST+0300             4.90175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
