
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-29 08:00:00 EEST+0300 2024-07-29 09:00:00 EEST+0300               4.006
	          2 2024-07-28 18:00:00 EEST+0300 2024-07-28 20:00:00 EEST+0300              3.8645
	          3 2024-07-28 18:00:00 EEST+0300 2024-07-28 21:00:00 EEST+0300            3.794333
	          4 2024-07-28 17:00:00 EEST+0300 2024-07-28 21:00:00 EEST+0300               3.692

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-29 04:00:00 EEST+0300 2024-07-29 05:00:00 EEST+0300              -0.157
	          2 2024-07-29 03:00:00 EEST+0300 2024-07-29 05:00:00 EEST+0300              -0.142
	          3 2024-07-29 03:00:00 EEST+0300 2024-07-29 06:00:00 EEST+0300              -0.137
	          4 2024-07-29 02:00:00 EEST+0300 2024-07-29 06:00:00 EEST+0300            -0.12575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
