
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-15 08:00:00 EEST+0300 2023-09-15 09:00:00 EEST+0300              31.011
	          2 2023-09-15 07:00:00 EEST+0300 2023-09-15 09:00:00 EEST+0300              30.993
	          3 2023-09-15 07:00:00 EEST+0300 2023-09-15 10:00:00 EEST+0300           29.569667
	          4 2023-09-15 08:00:00 EEST+0300 2023-09-15 12:00:00 EEST+0300            29.92675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-16 00:00:00 EEST+0300 2023-09-16 01:00:00 EEST+0300               0.746
	          2 2023-09-15 23:00:00 EEST+0300 2023-09-16 01:00:00 EEST+0300              0.9265
	          3 2023-09-15 22:00:00 EEST+0300 2023-09-16 01:00:00 EEST+0300               1.079
	          4 2023-09-15 21:00:00 EEST+0300 2023-09-16 01:00:00 EEST+0300              1.1865


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
