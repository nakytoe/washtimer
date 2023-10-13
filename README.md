
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-13 17:00:00 EEST+0300 2023-10-13 18:00:00 EEST+0300               0.528
	          2 2023-10-13 16:00:00 EEST+0300 2023-10-13 18:00:00 EEST+0300               0.527
	          3 2023-10-13 16:00:00 EEST+0300 2023-10-13 19:00:00 EEST+0300                 0.5
	          4 2023-10-13 16:00:00 EEST+0300 2023-10-13 20:00:00 EEST+0300             0.49725

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-14 06:00:00 EEST+0300 2023-10-14 07:00:00 EEST+0300              -0.437
	          2 2023-10-14 05:00:00 EEST+0300 2023-10-14 07:00:00 EEST+0300              -0.416
	          3 2023-10-14 04:00:00 EEST+0300 2023-10-14 07:00:00 EEST+0300           -0.391667
	          4 2023-10-14 04:00:00 EEST+0300 2023-10-14 08:00:00 EEST+0300            -0.36925


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
