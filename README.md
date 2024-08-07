
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-06 11:00:00 EEST+0300 2024-08-06 12:00:00 EEST+0300               3.493
	          2 2024-08-06 18:00:00 EEST+0300 2024-08-06 20:00:00 EEST+0300               3.454
	          3 2024-08-06 17:00:00 EEST+0300 2024-08-06 20:00:00 EEST+0300            3.439667
	          4 2024-08-06 17:00:00 EEST+0300 2024-08-06 21:00:00 EEST+0300             3.38575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-06 14:00:00 EEST+0300 2024-08-06 15:00:00 EEST+0300               2.025
	          2 2024-08-06 14:00:00 EEST+0300 2024-08-06 16:00:00 EEST+0300              2.0375
	          3 2024-08-06 13:00:00 EEST+0300 2024-08-06 16:00:00 EEST+0300            2.080333
	          4 2024-08-06 13:00:00 EEST+0300 2024-08-06 17:00:00 EEST+0300             2.17775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
