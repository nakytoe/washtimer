
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-14 19:00:00 EEST+0300 2023-10-14 20:00:00 EEST+0300               0.001
	          2 2023-10-14 18:00:00 EEST+0300 2023-10-14 20:00:00 EEST+0300              0.0005
	          3 2023-10-14 18:00:00 EEST+0300 2023-10-14 21:00:00 EEST+0300            0.000333
	          4 2023-10-15 18:00:00 EEST+0300 2023-10-15 22:00:00 EEST+0300             -0.0125

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-15 03:00:00 EEST+0300 2023-10-15 04:00:00 EEST+0300              -0.443
	          2 2023-10-15 02:00:00 EEST+0300 2023-10-15 04:00:00 EEST+0300             -0.4415
	          3 2023-10-15 01:00:00 EEST+0300 2023-10-15 04:00:00 EEST+0300               -0.44
	          4 2023-10-15 01:00:00 EEST+0300 2023-10-15 05:00:00 EEST+0300            -0.43875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
