
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-07 20:00:00 EEST+0300 2024-04-07 21:00:00 EEST+0300               3.704
	          2 2024-04-07 19:00:00 EEST+0300 2024-04-07 21:00:00 EEST+0300              3.5705
	          3 2024-04-07 19:00:00 EEST+0300 2024-04-07 22:00:00 EEST+0300               3.443
	          4 2024-04-07 19:00:00 EEST+0300 2024-04-07 23:00:00 EEST+0300              3.3145

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-07 15:00:00 EEST+0300 2024-04-07 16:00:00 EEST+0300                -1.0
	          2 2024-04-07 14:00:00 EEST+0300 2024-04-07 16:00:00 EEST+0300             -0.8275
	          3 2024-04-07 14:00:00 EEST+0300 2024-04-07 17:00:00 EEST+0300           -0.719667
	          4 2024-04-07 13:00:00 EEST+0300 2024-04-07 17:00:00 EEST+0300             -0.6395


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
