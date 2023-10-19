
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-19 09:00:00 EEST+0300 2023-10-19 10:00:00 EEST+0300               2.354
	          2 2023-10-19 09:00:00 EEST+0300 2023-10-19 11:00:00 EEST+0300                2.35
	          3 2023-10-19 09:00:00 EEST+0300 2023-10-19 12:00:00 EEST+0300            2.188333
	          4 2023-10-19 08:00:00 EEST+0300 2023-10-19 12:00:00 EEST+0300              2.0135

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-20 00:00:00 EEST+0300 2023-10-20 01:00:00 EEST+0300               0.527
	          2 2023-10-19 23:00:00 EEST+0300 2023-10-20 01:00:00 EEST+0300              0.6385
	          3 2023-10-19 22:00:00 EEST+0300 2023-10-20 01:00:00 EEST+0300               0.736
	          4 2023-10-19 21:00:00 EEST+0300 2023-10-20 01:00:00 EEST+0300             0.79375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
