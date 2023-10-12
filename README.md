
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-12 09:00:00 EEST+0300 2023-10-12 10:00:00 EEST+0300                 0.0
	          2 2023-10-12 09:00:00 EEST+0300 2023-10-12 11:00:00 EEST+0300                 0.0
	          3 2023-10-12 09:00:00 EEST+0300 2023-10-12 12:00:00 EEST+0300           -0.003667
	          4 2023-10-12 08:00:00 EEST+0300 2023-10-12 12:00:00 EEST+0300            -0.01175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-12 07:00:00 EEST+0300 2023-10-12 08:00:00 EEST+0300              -0.217
	          2 2023-10-12 14:00:00 EEST+0300 2023-10-12 16:00:00 EEST+0300              -0.209
	          3 2023-10-12 14:00:00 EEST+0300 2023-10-12 17:00:00 EEST+0300           -0.208333
	          4 2023-10-12 14:00:00 EEST+0300 2023-10-12 18:00:00 EEST+0300              -0.207


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
