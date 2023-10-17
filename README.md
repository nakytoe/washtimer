
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-17 09:00:00 EEST+0300 2023-10-17 10:00:00 EEST+0300                23.7
	          2 2023-10-17 08:00:00 EEST+0300 2023-10-17 10:00:00 EEST+0300              22.787
	          3 2023-10-17 08:00:00 EEST+0300 2023-10-17 11:00:00 EEST+0300              21.768
	          4 2023-10-17 07:00:00 EEST+0300 2023-10-17 11:00:00 EEST+0300               21.17

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-18 00:00:00 EEST+0300 2023-10-18 01:00:00 EEST+0300               1.064
	          2 2023-10-17 23:00:00 EEST+0300 2023-10-18 01:00:00 EEST+0300              1.5235
	          3 2023-10-17 22:00:00 EEST+0300 2023-10-18 01:00:00 EEST+0300            6.390333
	          4 2023-10-17 21:00:00 EEST+0300 2023-10-18 01:00:00 EEST+0300               8.203


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
