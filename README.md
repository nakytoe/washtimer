
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-17 09:00:00 EEST+0300 2024-05-17 10:00:00 EEST+0300               8.637
	          2 2024-05-17 08:00:00 EEST+0300 2024-05-17 10:00:00 EEST+0300               8.367
	          3 2024-05-17 08:00:00 EEST+0300 2024-05-17 11:00:00 EEST+0300               7.064
	          4 2024-05-17 07:00:00 EEST+0300 2024-05-17 11:00:00 EEST+0300             6.35375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-18 00:00:00 EEST+0300 2024-05-18 01:00:00 EEST+0300               -0.16
	          2 2024-05-17 23:00:00 EEST+0300 2024-05-18 01:00:00 EEST+0300             -0.0845
	          3 2024-05-17 22:00:00 EEST+0300 2024-05-18 01:00:00 EEST+0300              -0.005
	          4 2024-05-17 21:00:00 EEST+0300 2024-05-18 01:00:00 EEST+0300             0.12425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
