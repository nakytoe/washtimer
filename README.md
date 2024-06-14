
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-14 19:00:00 EEST+0300 2024-06-14 20:00:00 EEST+0300              22.331
	          2 2024-06-14 19:00:00 EEST+0300 2024-06-14 21:00:00 EEST+0300              20.202
	          3 2024-06-14 18:00:00 EEST+0300 2024-06-14 21:00:00 EEST+0300               17.05
	          4 2024-06-14 17:00:00 EEST+0300 2024-06-14 21:00:00 EEST+0300             15.3925

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-15 07:00:00 EEST+0300 2024-06-15 08:00:00 EEST+0300               0.423
	          2 2024-06-15 07:00:00 EEST+0300 2024-06-15 09:00:00 EEST+0300               0.558
	          3 2024-06-15 07:00:00 EEST+0300 2024-06-15 10:00:00 EEST+0300               0.584
	          4 2024-06-15 07:00:00 EEST+0300 2024-06-15 11:00:00 EEST+0300             0.59275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
