
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-18 20:00:00 EEST+0300 2024-07-18 21:00:00 EEST+0300               2.662
	          2 2024-07-18 19:00:00 EEST+0300 2024-07-18 21:00:00 EEST+0300              2.6055
	          3 2024-07-18 19:00:00 EEST+0300 2024-07-18 22:00:00 EEST+0300            2.563667
	          4 2024-07-18 18:00:00 EEST+0300 2024-07-18 22:00:00 EEST+0300             2.52425

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-18 02:00:00 EEST+0300 2024-07-18 03:00:00 EEST+0300              -0.999
	          2 2024-07-18 01:00:00 EEST+0300 2024-07-18 03:00:00 EEST+0300               -0.75
	          3 2024-07-18 01:00:00 EEST+0300 2024-07-18 04:00:00 EEST+0300           -0.666667
	          4 2024-07-18 01:00:00 EEST+0300 2024-07-18 05:00:00 EEST+0300            -0.57975


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
