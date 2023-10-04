
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-04 19:00:00 EEST+0300 2023-10-04 20:00:00 EEST+0300              16.406
	          2 2023-10-04 18:00:00 EEST+0300 2023-10-04 20:00:00 EEST+0300              9.7525
	          3 2023-10-04 17:00:00 EEST+0300 2023-10-04 20:00:00 EEST+0300            8.152667
	          4 2023-10-04 16:00:00 EEST+0300 2023-10-04 20:00:00 EEST+0300             6.39375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-05 00:00:00 EEST+0300 2023-10-05 01:00:00 EEST+0300              -0.016
	          2 2023-10-05 00:00:00 EEST+0300 2023-10-05 02:00:00 EEST+0300              -0.008
	          3 2023-10-05 00:00:00 EEST+0300 2023-10-05 03:00:00 EEST+0300           -0.006333
	          4 2023-10-05 00:00:00 EEST+0300 2023-10-05 04:00:00 EEST+0300            -0.00625


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
