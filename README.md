
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-04 20:00:00 EEST+0300 2024-06-04 21:00:00 EEST+0300              31.005
	          2 2024-06-04 20:00:00 EEST+0300 2024-06-04 22:00:00 EEST+0300                29.5
	          3 2024-06-04 19:00:00 EEST+0300 2024-06-04 22:00:00 EEST+0300           27.933667
	          4 2024-06-04 19:00:00 EEST+0300 2024-06-04 23:00:00 EEST+0300             27.1505

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-05 00:00:00 EEST+0300 2024-06-05 01:00:00 EEST+0300               3.441
	          2 2024-06-04 14:00:00 EEST+0300 2024-06-04 16:00:00 EEST+0300               6.536
	          3 2024-06-04 13:00:00 EEST+0300 2024-06-04 16:00:00 EEST+0300            7.144333
	          4 2024-06-04 12:00:00 EEST+0300 2024-06-04 16:00:00 EEST+0300              7.8185


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
