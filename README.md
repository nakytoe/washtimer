
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-11 18:00:00 EEST+0300 2023-10-11 19:00:00 EEST+0300               0.164
	          2 2023-10-11 17:00:00 EEST+0300 2023-10-11 19:00:00 EEST+0300              0.1545
	          3 2023-10-11 17:00:00 EEST+0300 2023-10-11 20:00:00 EEST+0300               0.139
	          4 2023-10-11 16:00:00 EEST+0300 2023-10-11 20:00:00 EEST+0300               0.106

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-12 04:00:00 EEST+0300 2023-10-12 05:00:00 EEST+0300              -1.039
	          2 2023-10-12 03:00:00 EEST+0300 2023-10-12 05:00:00 EEST+0300             -1.0235
	          3 2023-10-12 03:00:00 EEST+0300 2023-10-12 06:00:00 EEST+0300           -1.016667
	          4 2023-10-12 02:00:00 EEST+0300 2023-10-12 06:00:00 EEST+0300             -1.0125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
