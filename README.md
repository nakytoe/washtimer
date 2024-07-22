
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-22 16:00:00 EEST+0300 2024-07-22 17:00:00 EEST+0300                3.35
	          2 2024-07-22 18:00:00 EEST+0300 2024-07-22 20:00:00 EEST+0300              3.1935
	          3 2024-07-22 18:00:00 EEST+0300 2024-07-22 21:00:00 EEST+0300                3.16
	          4 2024-07-22 16:00:00 EEST+0300 2024-07-22 20:00:00 EEST+0300             3.14175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-23 03:00:00 EEST+0300 2024-07-23 04:00:00 EEST+0300               0.188
	          2 2024-07-23 03:00:00 EEST+0300 2024-07-23 05:00:00 EEST+0300              0.2715
	          3 2024-07-23 03:00:00 EEST+0300 2024-07-23 06:00:00 EEST+0300               0.543
	          4 2024-07-23 02:00:00 EEST+0300 2024-07-23 06:00:00 EEST+0300             0.71775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
