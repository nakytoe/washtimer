
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-09 08:00:00 EEST+0300 2024-05-09 09:00:00 EEST+0300              14.172
	          2 2024-05-09 08:00:00 EEST+0300 2024-05-09 10:00:00 EEST+0300              12.381
	          3 2024-05-09 08:00:00 EEST+0300 2024-05-09 11:00:00 EEST+0300               9.992
	          4 2024-05-09 07:00:00 EEST+0300 2024-05-09 11:00:00 EEST+0300             8.67975

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-10 00:00:00 EEST+0300 2024-05-10 01:00:00 EEST+0300              -0.001
	          2 2024-05-09 15:00:00 EEST+0300 2024-05-09 17:00:00 EEST+0300                 0.0
	          3 2024-05-09 14:00:00 EEST+0300 2024-05-09 17:00:00 EEST+0300            0.018333
	          4 2024-05-09 14:00:00 EEST+0300 2024-05-09 18:00:00 EEST+0300             0.10925


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
