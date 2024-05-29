
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-29 17:00:00 EEST+0300 2024-05-29 18:00:00 EEST+0300               30.99
	          2 2024-05-29 16:00:00 EEST+0300 2024-05-29 18:00:00 EEST+0300              27.895
	          3 2024-05-30 17:00:00 EEST+0300 2024-05-30 20:00:00 EEST+0300           25.821333
	          4 2024-05-30 17:00:00 EEST+0300 2024-05-30 21:00:00 EEST+0300            24.73075

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-30 02:00:00 EEST+0300 2024-05-30 03:00:00 EEST+0300               0.134
	          2 2024-05-30 02:00:00 EEST+0300 2024-05-30 04:00:00 EEST+0300              0.1445
	          3 2024-05-30 02:00:00 EEST+0300 2024-05-30 05:00:00 EEST+0300               0.171
	          4 2024-05-30 01:00:00 EEST+0300 2024-05-30 05:00:00 EEST+0300             0.18475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
