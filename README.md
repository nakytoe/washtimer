
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-10 09:00:00 EEST+0300 2024-04-10 10:00:00 EEST+0300               2.411
	          2 2024-04-10 08:00:00 EEST+0300 2024-04-10 10:00:00 EEST+0300              2.0475
	          3 2024-04-10 08:00:00 EEST+0300 2024-04-10 11:00:00 EEST+0300                1.57
	          4 2024-04-10 07:00:00 EEST+0300 2024-04-10 11:00:00 EEST+0300             1.27325

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-11 00:00:00 EEST+0300 2024-04-11 01:00:00 EEST+0300              -0.309
	          2 2024-04-10 23:00:00 EEST+0300 2024-04-11 01:00:00 EEST+0300              -0.278
	          3 2024-04-10 22:00:00 EEST+0300 2024-04-11 01:00:00 EEST+0300              -0.261
	          4 2024-04-10 21:00:00 EEST+0300 2024-04-11 01:00:00 EEST+0300              -0.246


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
