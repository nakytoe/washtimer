
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-01 20:00:00 EEST+0300 2023-10-01 21:00:00 EEST+0300               5.829
	          2 2023-10-01 19:00:00 EEST+0300 2023-10-01 21:00:00 EEST+0300              3.5855
	          3 2023-10-01 19:00:00 EEST+0300 2023-10-01 22:00:00 EEST+0300            2.596333
	          4 2023-10-01 19:00:00 EEST+0300 2023-10-01 23:00:00 EEST+0300              2.0985

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-01 07:00:00 EEST+0300 2023-10-01 08:00:00 EEST+0300                -0.2
	          2 2023-10-01 07:00:00 EEST+0300 2023-10-01 09:00:00 EEST+0300             -0.1895
	          3 2023-10-01 07:00:00 EEST+0300 2023-10-01 10:00:00 EEST+0300              -0.162
	          4 2023-10-01 07:00:00 EEST+0300 2023-10-01 11:00:00 EEST+0300             -0.1255


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
