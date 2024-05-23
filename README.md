
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-23 09:00:00 EEST+0300 2024-05-23 10:00:00 EEST+0300                2.78
	          2 2024-05-23 09:00:00 EEST+0300 2024-05-23 11:00:00 EEST+0300               2.328
	          3 2024-05-23 08:00:00 EEST+0300 2024-05-23 11:00:00 EEST+0300            1.996333
	          4 2024-05-23 08:00:00 EEST+0300 2024-05-23 12:00:00 EEST+0300             1.71375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-24 00:00:00 EEST+0300 2024-05-24 01:00:00 EEST+0300              -0.085
	          2 2024-05-23 23:00:00 EEST+0300 2024-05-24 01:00:00 EEST+0300             -0.0425
	          3 2024-05-23 22:00:00 EEST+0300 2024-05-24 01:00:00 EEST+0300               0.034
	          4 2024-05-23 21:00:00 EEST+0300 2024-05-24 01:00:00 EEST+0300             0.11475


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
