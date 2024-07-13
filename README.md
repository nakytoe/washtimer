
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-13 20:00:00 EEST+0300 2024-07-13 21:00:00 EEST+0300               3.257
	          2 2024-07-13 19:00:00 EEST+0300 2024-07-13 21:00:00 EEST+0300                3.02
	          3 2024-07-13 19:00:00 EEST+0300 2024-07-13 22:00:00 EEST+0300               2.912
	          4 2024-07-13 19:00:00 EEST+0300 2024-07-13 23:00:00 EEST+0300              2.7315

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-14 15:00:00 EEST+0300 2024-07-14 16:00:00 EEST+0300              -0.641
	          2 2024-07-14 15:00:00 EEST+0300 2024-07-14 17:00:00 EEST+0300             -0.5885
	          3 2024-07-14 14:00:00 EEST+0300 2024-07-14 17:00:00 EEST+0300           -0.564333
	          4 2024-07-14 13:00:00 EEST+0300 2024-07-14 17:00:00 EEST+0300            -0.52875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
