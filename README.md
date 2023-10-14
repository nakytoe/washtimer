
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
	          4 2023-10-14 17:00:00 EEST+0300 2023-10-14 21:00:00 EEST+0300            -0.02525

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-15 00:00:00 EEST+0300 2023-10-15 01:00:00 EEST+0300              -0.308
	          2 2023-10-14 07:00:00 EEST+0300 2023-10-14 09:00:00 EEST+0300              -0.281
	          3 2023-10-14 07:00:00 EEST+0300 2023-10-14 10:00:00 EEST+0300              -0.255
	          4 2023-10-14 07:00:00 EEST+0300 2023-10-14 11:00:00 EEST+0300              -0.242


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
