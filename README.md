
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-14 11:00:00 EEST+0300 2024-04-14 12:00:00 EEST+0300               3.832
	          2 2024-04-14 11:00:00 EEST+0300 2024-04-14 13:00:00 EEST+0300              3.7675
	          3 2024-04-14 10:00:00 EEST+0300 2024-04-14 13:00:00 EEST+0300            3.574667
	          4 2024-04-14 10:00:00 EEST+0300 2024-04-14 14:00:00 EEST+0300             3.37325

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-15 00:00:00 EEST+0300 2024-04-15 01:00:00 EEST+0300              -0.015
	          2 2024-04-14 23:00:00 EEST+0300 2024-04-15 01:00:00 EEST+0300               -0.01
	          3 2024-04-14 22:00:00 EEST+0300 2024-04-15 01:00:00 EEST+0300           -0.006667
	          4 2024-04-14 21:00:00 EEST+0300 2024-04-15 01:00:00 EEST+0300                0.04


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
