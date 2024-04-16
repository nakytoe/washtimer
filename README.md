
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-16 20:00:00 EEST+0300 2024-04-16 21:00:00 EEST+0300              14.135
	          2 2024-04-16 20:00:00 EEST+0300 2024-04-16 22:00:00 EEST+0300             13.7885
	          3 2024-04-16 19:00:00 EEST+0300 2024-04-16 22:00:00 EEST+0300              13.033
	          4 2024-04-16 19:00:00 EEST+0300 2024-04-16 23:00:00 EEST+0300            11.63475

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-16 16:00:00 EEST+0300 2024-04-16 17:00:00 EEST+0300               6.018
	          2 2024-04-16 16:00:00 EEST+0300 2024-04-16 18:00:00 EEST+0300              6.2125
	          3 2024-04-16 16:00:00 EEST+0300 2024-04-16 19:00:00 EEST+0300               6.415
	          4 2024-04-16 16:00:00 EEST+0300 2024-04-16 20:00:00 EEST+0300             7.69175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
