
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-09 19:00:00 EEST+0300 2023-08-09 20:00:00 EEST+0300               1.864
	          2 2023-08-09 19:00:00 EEST+0300 2023-08-09 21:00:00 EEST+0300              1.8345
	          3 2023-08-09 19:00:00 EEST+0300 2023-08-09 22:00:00 EEST+0300            1.638667
	          4 2023-08-09 19:00:00 EEST+0300 2023-08-09 23:00:00 EEST+0300             1.56575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-09 07:00:00 EEST+0300 2023-08-09 08:00:00 EEST+0300               0.001
	          2 2023-08-09 07:00:00 EEST+0300 2023-08-09 09:00:00 EEST+0300                0.16
	          3 2023-08-09 07:00:00 EEST+0300 2023-08-09 10:00:00 EEST+0300            0.257667
	          4 2023-08-09 07:00:00 EEST+0300 2023-08-09 11:00:00 EEST+0300              0.3365


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
