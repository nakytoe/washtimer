
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-24 21:00:00 EEST+0300 2024-04-24 22:00:00 EEST+0300              17.787
	          2 2024-04-24 20:00:00 EEST+0300 2024-04-24 22:00:00 EEST+0300              17.276
	          3 2024-04-24 20:00:00 EEST+0300 2024-04-24 23:00:00 EEST+0300           16.270333
	          4 2024-04-24 19:00:00 EEST+0300 2024-04-24 23:00:00 EEST+0300              15.428

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-25 15:00:00 EEST+0300 2024-04-25 16:00:00 EEST+0300               8.284
	          2 2024-04-25 15:00:00 EEST+0300 2024-04-25 17:00:00 EEST+0300              8.4435
	          3 2024-04-25 15:00:00 EEST+0300 2024-04-25 18:00:00 EEST+0300            8.638333
	          4 2024-04-25 14:00:00 EEST+0300 2024-04-25 18:00:00 EEST+0300             8.81525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
