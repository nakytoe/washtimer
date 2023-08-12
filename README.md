
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-13 20:00:00 EEST+0300 2023-08-13 21:00:00 EEST+0300               2.417
	          2 2023-08-13 19:00:00 EEST+0300 2023-08-13 21:00:00 EEST+0300              2.4155
	          3 2023-08-13 18:00:00 EEST+0300 2023-08-13 21:00:00 EEST+0300               2.408
	          4 2023-08-13 18:00:00 EEST+0300 2023-08-13 22:00:00 EEST+0300              2.3845

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-13 14:00:00 EEST+0300 2023-08-13 15:00:00 EEST+0300               0.136
	          2 2023-08-13 14:00:00 EEST+0300 2023-08-13 16:00:00 EEST+0300              0.1615
	          3 2023-08-13 13:00:00 EEST+0300 2023-08-13 16:00:00 EEST+0300               0.356
	          4 2023-08-13 13:00:00 EEST+0300 2023-08-13 17:00:00 EEST+0300              0.4815


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
