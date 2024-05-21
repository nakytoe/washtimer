
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-21 09:00:00 EEST+0300 2024-05-21 10:00:00 EEST+0300                6.78
	          2 2024-05-21 08:00:00 EEST+0300 2024-05-21 10:00:00 EEST+0300              6.4585
	          3 2024-05-21 08:00:00 EEST+0300 2024-05-21 11:00:00 EEST+0300               5.768
	          4 2024-05-21 07:00:00 EEST+0300 2024-05-21 11:00:00 EEST+0300               5.339

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-22 00:00:00 EEST+0300 2024-05-22 01:00:00 EEST+0300               1.033
	          2 2024-05-21 23:00:00 EEST+0300 2024-05-22 01:00:00 EEST+0300               1.381
	          3 2024-05-21 22:00:00 EEST+0300 2024-05-22 01:00:00 EEST+0300               2.169
	          4 2024-05-21 13:00:00 EEST+0300 2024-05-21 17:00:00 EEST+0300             2.31825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
