
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-12 19:00:00 EEST+0300 2023-08-12 20:00:00 EEST+0300               2.225
	          2 2023-08-12 19:00:00 EEST+0300 2023-08-12 21:00:00 EEST+0300               2.221
	          3 2023-08-12 18:00:00 EEST+0300 2023-08-12 21:00:00 EEST+0300            2.200667
	          4 2023-08-12 18:00:00 EEST+0300 2023-08-12 22:00:00 EEST+0300             2.18025

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-12 07:00:00 EEST+0300 2023-08-12 08:00:00 EEST+0300               0.662
	          2 2023-08-12 15:00:00 EEST+0300 2023-08-12 17:00:00 EEST+0300               0.801
	          3 2023-08-12 14:00:00 EEST+0300 2023-08-12 17:00:00 EEST+0300               0.952
	          4 2023-08-12 13:00:00 EEST+0300 2023-08-12 17:00:00 EEST+0300              1.0515


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
