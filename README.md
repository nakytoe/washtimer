
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-15 09:00:00 EEST+0300 2024-04-15 10:00:00 EEST+0300                12.9
	          2 2024-04-15 08:00:00 EEST+0300 2024-04-15 10:00:00 EEST+0300             10.4325
	          3 2024-04-15 08:00:00 EEST+0300 2024-04-15 11:00:00 EEST+0300            9.002667
	          4 2024-04-15 08:00:00 EEST+0300 2024-04-15 12:00:00 EEST+0300             8.29575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-15 01:00:00 EEST+0300 2024-04-15 02:00:00 EEST+0300              -0.173
	          2 2024-04-15 01:00:00 EEST+0300 2024-04-15 03:00:00 EEST+0300              -0.171
	          3 2024-04-15 01:00:00 EEST+0300 2024-04-15 04:00:00 EEST+0300           -0.133333
	          4 2024-04-15 00:00:00 EEST+0300 2024-04-15 04:00:00 EEST+0300            -0.10375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
