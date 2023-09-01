
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-01 09:00:00 EEST+0300 2023-09-01 10:00:00 EEST+0300              24.794
	          2 2023-09-01 20:00:00 EEST+0300 2023-09-01 22:00:00 EEST+0300              23.533
	          3 2023-09-01 09:00:00 EEST+0300 2023-09-01 12:00:00 EEST+0300           21.973667
	          4 2023-09-01 08:00:00 EEST+0300 2023-09-01 12:00:00 EEST+0300              21.219

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-01 15:00:00 EEST+0300 2023-09-01 16:00:00 EEST+0300              11.014
	          2 2023-09-01 14:00:00 EEST+0300 2023-09-01 16:00:00 EEST+0300              11.019
	          3 2023-09-01 14:00:00 EEST+0300 2023-09-01 17:00:00 EEST+0300           11.131667
	          4 2023-09-01 13:00:00 EEST+0300 2023-09-01 17:00:00 EEST+0300            11.20125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
