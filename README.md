
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-15 19:00:00 EEST+0300 2024-07-15 20:00:00 EEST+0300               3.708
	          2 2024-07-15 19:00:00 EEST+0300 2024-07-15 21:00:00 EEST+0300               3.695
	          3 2024-07-15 18:00:00 EEST+0300 2024-07-15 21:00:00 EEST+0300            3.657333
	          4 2024-07-15 18:00:00 EEST+0300 2024-07-15 22:00:00 EEST+0300             3.63825

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-15 14:00:00 EEST+0300 2024-07-15 15:00:00 EEST+0300                1.24
	          2 2024-07-15 13:00:00 EEST+0300 2024-07-15 15:00:00 EEST+0300               1.604
	          3 2024-07-15 13:00:00 EEST+0300 2024-07-15 16:00:00 EEST+0300            1.829333
	          4 2024-07-15 12:00:00 EEST+0300 2024-07-15 16:00:00 EEST+0300               1.993


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
