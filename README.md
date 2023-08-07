
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-07 10:00:00 EEST+0300 2023-08-07 11:00:00 EEST+0300               0.615
	          2 2023-08-07 09:00:00 EEST+0300 2023-08-07 11:00:00 EEST+0300              0.5805
	          3 2023-08-07 09:00:00 EEST+0300 2023-08-07 12:00:00 EEST+0300            0.555333
	          4 2023-08-07 08:00:00 EEST+0300 2023-08-07 12:00:00 EEST+0300             0.48775

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-07 16:00:00 EEST+0300 2023-08-07 17:00:00 EEST+0300              -0.114
	          2 2023-08-07 15:00:00 EEST+0300 2023-08-07 17:00:00 EEST+0300             -0.1125
	          3 2023-08-07 15:00:00 EEST+0300 2023-08-07 18:00:00 EEST+0300              -0.105
	          4 2023-08-07 14:00:00 EEST+0300 2023-08-07 18:00:00 EEST+0300              -0.099


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
