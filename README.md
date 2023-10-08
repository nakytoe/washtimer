
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-09 20:00:00 EEST+0300 2023-10-09 21:00:00 EEST+0300              27.491
	          2 2023-10-09 19:00:00 EEST+0300 2023-10-09 21:00:00 EEST+0300              25.477
	          3 2023-10-09 19:00:00 EEST+0300 2023-10-09 22:00:00 EEST+0300           24.427667
	          4 2023-10-09 19:00:00 EEST+0300 2023-10-09 23:00:00 EEST+0300             22.3375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-08 16:00:00 EEST+0300 2023-10-08 17:00:00 EEST+0300                0.31
	          2 2023-10-08 16:00:00 EEST+0300 2023-10-08 18:00:00 EEST+0300              0.3615
	          3 2023-10-08 16:00:00 EEST+0300 2023-10-08 19:00:00 EEST+0300               0.446
	          4 2023-10-09 01:00:00 EEST+0300 2023-10-09 05:00:00 EEST+0300             0.51425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
