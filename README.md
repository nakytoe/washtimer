
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-10 19:00:00 EEST+0300 2024-07-10 20:00:00 EEST+0300               3.239
	          2 2024-07-10 18:00:00 EEST+0300 2024-07-10 20:00:00 EEST+0300               3.196
	          3 2024-07-10 18:00:00 EEST+0300 2024-07-10 21:00:00 EEST+0300            3.176667
	          4 2024-07-10 17:00:00 EEST+0300 2024-07-10 21:00:00 EEST+0300               3.124

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-11 04:00:00 EEST+0300 2024-07-11 05:00:00 EEST+0300                -1.0
	          2 2024-07-11 04:00:00 EEST+0300 2024-07-11 06:00:00 EEST+0300             -0.9985
	          3 2024-07-11 03:00:00 EEST+0300 2024-07-11 06:00:00 EEST+0300           -0.942667
	          4 2024-07-11 02:00:00 EEST+0300 2024-07-11 06:00:00 EEST+0300              -0.782


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
