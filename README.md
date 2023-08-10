
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-11 10:00:00 EEST+0300 2023-08-11 11:00:00 EEST+0300               2.923
	          2 2023-08-11 09:00:00 EEST+0300 2023-08-11 11:00:00 EEST+0300              2.9075
	          3 2023-08-11 09:00:00 EEST+0300 2023-08-11 12:00:00 EEST+0300               2.823
	          4 2023-08-11 08:00:00 EEST+0300 2023-08-11 12:00:00 EEST+0300              2.7235

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-11 00:00:00 EEST+0300 2023-08-11 01:00:00 EEST+0300               1.235
	          2 2023-08-11 04:00:00 EEST+0300 2023-08-11 06:00:00 EEST+0300              1.3535
	          3 2023-08-11 03:00:00 EEST+0300 2023-08-11 06:00:00 EEST+0300               1.377
	          4 2023-08-11 02:00:00 EEST+0300 2023-08-11 06:00:00 EEST+0300              1.4445


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
