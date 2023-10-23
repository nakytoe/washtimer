
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-23 07:00:00 EEST+0300 2023-10-23 08:00:00 EEST+0300              31.004
	          2 2023-10-23 07:00:00 EEST+0300 2023-10-23 09:00:00 EEST+0300              31.003
	          3 2023-10-23 07:00:00 EEST+0300 2023-10-23 10:00:00 EEST+0300           31.002333
	          4 2023-10-23 07:00:00 EEST+0300 2023-10-23 11:00:00 EEST+0300            29.45175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-24 00:00:00 EEST+0300 2023-10-24 01:00:00 EEST+0300               2.978
	          2 2023-10-23 23:00:00 EEST+0300 2023-10-24 01:00:00 EEST+0300              3.4695
	          3 2023-10-23 22:00:00 EEST+0300 2023-10-24 01:00:00 EEST+0300            4.918667
	          4 2023-10-23 21:00:00 EEST+0300 2023-10-24 01:00:00 EEST+0300               5.756


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
