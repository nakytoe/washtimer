
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
	          1 2023-10-28 00:00:00 EEST+0300 2023-10-28 01:00:00 EEST+0300               5.447
	          2 2023-10-27 23:00:00 EEST+0300 2023-10-28 01:00:00 EEST+0300              5.5805
	          3 2023-10-27 22:00:00 EEST+0300 2023-10-28 01:00:00 EEST+0300            6.555667
	          4 2023-10-27 21:00:00 EEST+0300 2023-10-28 01:00:00 EEST+0300             7.20575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
