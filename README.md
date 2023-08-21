
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-21 19:00:00 EEST+0300 2023-08-21 20:00:00 EEST+0300              68.194
	          2 2023-08-21 08:00:00 EEST+0300 2023-08-21 10:00:00 EEST+0300             54.2505
	          3 2023-08-21 09:00:00 EEST+0300 2023-08-21 12:00:00 EEST+0300           53.031333
	          4 2023-08-21 08:00:00 EEST+0300 2023-08-21 12:00:00 EEST+0300            49.85125

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-22 00:00:00 EEST+0300 2023-08-22 01:00:00 EEST+0300               14.26
	          2 2023-08-21 23:00:00 EEST+0300 2023-08-22 01:00:00 EEST+0300             15.5625
	          3 2023-08-21 22:00:00 EEST+0300 2023-08-22 01:00:00 EEST+0300           17.360333
	          4 2023-08-21 21:00:00 EEST+0300 2023-08-22 01:00:00 EEST+0300            19.35625


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
