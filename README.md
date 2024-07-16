
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-16 19:00:00 EEST+0300 2024-07-16 20:00:00 EEST+0300                3.59
	          2 2024-07-16 19:00:00 EEST+0300 2024-07-16 21:00:00 EEST+0300               3.556
	          3 2024-07-16 19:00:00 EEST+0300 2024-07-16 22:00:00 EEST+0300            3.502333
	          4 2024-07-16 19:00:00 EEST+0300 2024-07-16 23:00:00 EEST+0300             3.44075

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-18 00:00:00 EEST+0300 2024-07-18 01:00:00 EEST+0300               -0.28
	          2 2024-07-17 23:00:00 EEST+0300 2024-07-18 01:00:00 EEST+0300             -0.1825
	          3 2024-07-17 22:00:00 EEST+0300 2024-07-18 01:00:00 EEST+0300           -0.122667
	          4 2024-07-17 21:00:00 EEST+0300 2024-07-18 01:00:00 EEST+0300            -0.09225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
