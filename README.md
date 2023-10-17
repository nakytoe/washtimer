
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-17 19:00:00 EEST+0300 2023-10-17 20:00:00 EEST+0300              21.892
	          2 2023-10-17 18:00:00 EEST+0300 2023-10-17 20:00:00 EEST+0300              21.752
	          3 2023-10-17 18:00:00 EEST+0300 2023-10-17 21:00:00 EEST+0300           21.700667
	          4 2023-10-17 17:00:00 EEST+0300 2023-10-17 21:00:00 EEST+0300              21.091

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-19 00:00:00 EEST+0300 2023-10-19 01:00:00 EEST+0300               0.844
	          2 2023-10-18 03:00:00 EEST+0300 2023-10-18 05:00:00 EEST+0300              0.8885
	          3 2023-10-18 02:00:00 EEST+0300 2023-10-18 05:00:00 EEST+0300            0.892667
	          4 2023-10-18 01:00:00 EEST+0300 2023-10-18 05:00:00 EEST+0300             0.89825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
