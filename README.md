
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-26 19:00:00 EEST+0300 2023-08-26 20:00:00 EEST+0300              21.034
	          2 2023-08-26 18:00:00 EEST+0300 2023-08-26 20:00:00 EEST+0300              19.559
	          3 2023-08-26 18:00:00 EEST+0300 2023-08-26 21:00:00 EEST+0300           18.200333
	          4 2023-08-26 18:00:00 EEST+0300 2023-08-26 22:00:00 EEST+0300             17.2135

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-27 00:00:00 EEST+0300 2023-08-27 01:00:00 EEST+0300               2.363
	          2 2023-08-26 23:00:00 EEST+0300 2023-08-27 01:00:00 EEST+0300              5.6575
	          3 2023-08-26 22:00:00 EEST+0300 2023-08-27 01:00:00 EEST+0300                8.57
	          4 2023-08-26 21:00:00 EEST+0300 2023-08-27 01:00:00 EEST+0300             9.99075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
