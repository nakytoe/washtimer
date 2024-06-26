
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-27 09:00:00 EEST+0300 2024-06-27 10:00:00 EEST+0300                4.36
	          2 2024-06-27 09:00:00 EEST+0300 2024-06-27 11:00:00 EEST+0300               4.337
	          3 2024-06-26 19:00:00 EEST+0300 2024-06-26 22:00:00 EEST+0300            4.285333
	          4 2024-06-26 19:00:00 EEST+0300 2024-06-26 23:00:00 EEST+0300             4.25875

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-28 00:00:00 EEST+0300 2024-06-28 01:00:00 EEST+0300               0.435
	          2 2024-06-27 23:00:00 EEST+0300 2024-06-28 01:00:00 EEST+0300               1.153
	          3 2024-06-27 22:00:00 EEST+0300 2024-06-28 01:00:00 EEST+0300            1.691333
	          4 2024-06-27 21:00:00 EEST+0300 2024-06-28 01:00:00 EEST+0300               2.054


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
