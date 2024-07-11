
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-12 00:00:00 EEST+0300 2024-07-12 01:00:00 EEST+0300               0.232
	          2 2024-07-11 23:00:00 EEST+0300 2024-07-12 01:00:00 EEST+0300              0.1435
	          3 2024-07-11 22:00:00 EEST+0300 2024-07-12 01:00:00 EEST+0300            0.095667
	          4 2024-07-11 21:00:00 EEST+0300 2024-07-12 01:00:00 EEST+0300             0.07025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-11 07:00:00 EEST+0300 2024-07-11 08:00:00 EEST+0300              -0.085
	          2 2024-07-11 15:00:00 EEST+0300 2024-07-11 17:00:00 EEST+0300              -0.055
	          3 2024-07-11 14:00:00 EEST+0300 2024-07-11 17:00:00 EEST+0300              -0.043
	          4 2024-07-11 14:00:00 EEST+0300 2024-07-11 18:00:00 EEST+0300              -0.035


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
