
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-09 22:00:00 EEST+0300 2024-06-09 23:00:00 EEST+0300               2.164
	          2 2024-06-09 22:00:00 EEST+0300 2024-06-10 00:00:00 EEST+0300               2.116
	          3 2024-06-09 22:00:00 EEST+0300 2024-06-10 01:00:00 EEST+0300            2.064667
	          4 2024-06-09 21:00:00 EEST+0300 2024-06-10 01:00:00 EEST+0300              1.9435

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-09 16:00:00 EEST+0300 2024-06-09 17:00:00 EEST+0300              -0.658
	          2 2024-06-09 15:00:00 EEST+0300 2024-06-09 17:00:00 EEST+0300              -0.587
	          3 2024-06-09 15:00:00 EEST+0300 2024-06-09 18:00:00 EEST+0300           -0.557667
	          4 2024-06-09 14:00:00 EEST+0300 2024-06-09 18:00:00 EEST+0300            -0.49325


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
