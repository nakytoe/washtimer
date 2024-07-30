
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-31 19:00:00 EEST+0300 2024-07-31 20:00:00 EEST+0300               4.135
	          2 2024-07-31 18:00:00 EEST+0300 2024-07-31 20:00:00 EEST+0300              4.0875
	          3 2024-07-31 18:00:00 EEST+0300 2024-07-31 21:00:00 EEST+0300            4.054667
	          4 2024-07-31 17:00:00 EEST+0300 2024-07-31 21:00:00 EEST+0300               3.971

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-01 00:00:00 EEST+0300 2024-08-01 01:00:00 EEST+0300              -0.001
	          2 2024-07-31 23:00:00 EEST+0300 2024-08-01 01:00:00 EEST+0300               0.309
	          3 2024-07-31 04:00:00 EEST+0300 2024-07-31 07:00:00 EEST+0300               0.615
	          4 2024-07-31 03:00:00 EEST+0300 2024-07-31 07:00:00 EEST+0300             0.61575


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
