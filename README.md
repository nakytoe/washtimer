
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-04 11:00:00 EEST+0300 2023-08-04 12:00:00 EEST+0300               3.125
	          2 2023-08-04 10:00:00 EEST+0300 2023-08-04 12:00:00 EEST+0300                 3.1
	          3 2023-08-04 10:00:00 EEST+0300 2023-08-04 13:00:00 EEST+0300            3.091333
	          4 2023-08-04 10:00:00 EEST+0300 2023-08-04 14:00:00 EEST+0300             3.07325

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-05 00:00:00 EEST+0300 2023-08-05 01:00:00 EEST+0300                2.11
	          2 2023-08-04 23:00:00 EEST+0300 2023-08-05 01:00:00 EEST+0300               2.177
	          3 2023-08-04 22:00:00 EEST+0300 2023-08-05 01:00:00 EEST+0300               2.316
	          4 2023-08-04 21:00:00 EEST+0300 2023-08-05 01:00:00 EEST+0300             2.45875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
