
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-12 21:00:00 EEST+0300 2024-06-12 22:00:00 EEST+0300              19.188
	          2 2024-06-12 21:00:00 EEST+0300 2024-06-12 23:00:00 EEST+0300              19.085
	          3 2024-06-12 20:00:00 EEST+0300 2024-06-12 23:00:00 EEST+0300           18.510667
	          4 2024-06-12 20:00:00 EEST+0300 2024-06-13 00:00:00 EEST+0300            18.06675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-13 00:00:00 EEST+0300 2024-06-13 01:00:00 EEST+0300               5.108
	          2 2024-06-12 15:00:00 EEST+0300 2024-06-12 17:00:00 EEST+0300               5.952
	          3 2024-06-12 14:00:00 EEST+0300 2024-06-12 17:00:00 EEST+0300            6.069667
	          4 2024-06-12 13:00:00 EEST+0300 2024-06-12 17:00:00 EEST+0300               6.405


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
