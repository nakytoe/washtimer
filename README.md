
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-19 11:00:00 EEST+0300 2023-08-19 12:00:00 EEST+0300              26.326
	          2 2023-08-19 10:00:00 EEST+0300 2023-08-19 12:00:00 EEST+0300              22.464
	          3 2023-08-19 19:00:00 EEST+0300 2023-08-19 22:00:00 EEST+0300           20.173333
	          4 2023-08-19 17:00:00 EEST+0300 2023-08-19 21:00:00 EEST+0300            19.75775

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-20 00:00:00 EEST+0300 2023-08-20 01:00:00 EEST+0300               5.041
	          2 2023-08-19 23:00:00 EEST+0300 2023-08-20 01:00:00 EEST+0300             10.1905
	          3 2023-08-19 22:00:00 EEST+0300 2023-08-20 01:00:00 EEST+0300              12.547
	          4 2023-08-19 21:00:00 EEST+0300 2023-08-20 01:00:00 EEST+0300             13.5875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
