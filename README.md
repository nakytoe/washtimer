
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-03 09:00:00 EEST+0300 2023-10-03 10:00:00 EEST+0300              16.652
	          2 2023-10-03 09:00:00 EEST+0300 2023-10-03 11:00:00 EEST+0300             15.1485
	          3 2023-10-03 09:00:00 EEST+0300 2023-10-03 12:00:00 EEST+0300              14.646
	          4 2023-10-03 08:00:00 EEST+0300 2023-10-03 12:00:00 EEST+0300            14.39475

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-04 00:00:00 EEST+0300 2023-10-04 01:00:00 EEST+0300               0.091
	          2 2023-10-03 23:00:00 EEST+0300 2023-10-04 01:00:00 EEST+0300              0.2125
	          3 2023-10-03 22:00:00 EEST+0300 2023-10-04 01:00:00 EEST+0300            0.310667
	          4 2023-10-03 21:00:00 EEST+0300 2023-10-04 01:00:00 EEST+0300             0.39975


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
