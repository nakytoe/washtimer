
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-10 20:00:00 EEST+0300 2023-09-10 21:00:00 EEST+0300               4.985
	          2 2023-09-10 20:00:00 EEST+0300 2023-09-10 22:00:00 EEST+0300               4.205
	          3 2023-09-10 19:00:00 EEST+0300 2023-09-10 22:00:00 EEST+0300            3.876333
	          4 2023-09-10 18:00:00 EEST+0300 2023-09-10 22:00:00 EEST+0300              3.6535

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-10 01:00:00 EEST+0300 2023-09-10 02:00:00 EEST+0300              -0.202
	          2 2023-09-10 01:00:00 EEST+0300 2023-09-10 03:00:00 EEST+0300             -0.1905
	          3 2023-09-10 01:00:00 EEST+0300 2023-09-10 04:00:00 EEST+0300           -0.165667
	          4 2023-09-10 00:00:00 EEST+0300 2023-09-10 04:00:00 EEST+0300            -0.15125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
