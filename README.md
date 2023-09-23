
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-24 19:00:00 EEST+0300 2023-09-24 20:00:00 EEST+0300               1.023
	          2 2023-09-24 19:00:00 EEST+0300 2023-09-24 21:00:00 EEST+0300                 1.0
	          3 2023-09-24 18:00:00 EEST+0300 2023-09-24 21:00:00 EEST+0300            0.980667
	          4 2023-09-24 18:00:00 EEST+0300 2023-09-24 22:00:00 EEST+0300             0.90725

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-24 14:00:00 EEST+0300 2023-09-24 15:00:00 EEST+0300              -0.262
	          2 2023-09-24 14:00:00 EEST+0300 2023-09-24 16:00:00 EEST+0300               -0.23
	          3 2023-09-24 13:00:00 EEST+0300 2023-09-24 16:00:00 EEST+0300           -0.154333
	          4 2023-09-24 13:00:00 EEST+0300 2023-09-24 17:00:00 EEST+0300             -0.1165


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
