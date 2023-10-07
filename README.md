
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-08 20:00:00 EEST+0300 2023-10-08 21:00:00 EEST+0300               1.409
	          2 2023-10-08 20:00:00 EEST+0300 2023-10-08 22:00:00 EEST+0300               1.272
	          3 2023-10-08 19:00:00 EEST+0300 2023-10-08 22:00:00 EEST+0300            1.166667
	          4 2023-10-08 19:00:00 EEST+0300 2023-10-08 23:00:00 EEST+0300             1.09925

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-08 04:00:00 EEST+0300 2023-10-08 05:00:00 EEST+0300              -0.207
	          2 2023-10-08 04:00:00 EEST+0300 2023-10-08 06:00:00 EEST+0300              -0.206
	          3 2023-10-08 03:00:00 EEST+0300 2023-10-08 06:00:00 EEST+0300           -0.205333
	          4 2023-10-08 02:00:00 EEST+0300 2023-10-08 06:00:00 EEST+0300            -0.20375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
