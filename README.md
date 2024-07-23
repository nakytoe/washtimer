
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-23 09:00:00 EEST+0300 2024-07-23 10:00:00 EEST+0300               3.039
	          2 2024-07-23 09:00:00 EEST+0300 2024-07-23 11:00:00 EEST+0300               3.015
	          3 2024-07-23 08:00:00 EEST+0300 2024-07-23 11:00:00 EEST+0300               2.999
	          4 2024-07-23 08:00:00 EEST+0300 2024-07-23 12:00:00 EEST+0300               2.973

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-24 00:00:00 EEST+0300 2024-07-24 01:00:00 EEST+0300               2.611
	          2 2024-07-23 14:00:00 EEST+0300 2024-07-23 16:00:00 EEST+0300              2.6305
	          3 2024-07-23 13:00:00 EEST+0300 2024-07-23 16:00:00 EEST+0300               2.646
	          4 2024-07-23 13:00:00 EEST+0300 2024-07-23 17:00:00 EEST+0300              2.6615


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
