
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-27 09:00:00 EEST+0300 2024-05-27 10:00:00 EEST+0300               1.477
	          2 2024-05-27 09:00:00 EEST+0300 2024-05-27 11:00:00 EEST+0300              1.2225
	          3 2024-05-27 08:00:00 EEST+0300 2024-05-27 11:00:00 EEST+0300            1.133667
	          4 2024-05-27 08:00:00 EEST+0300 2024-05-27 12:00:00 EEST+0300              0.9815

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-28 00:00:00 EEST+0300 2024-05-28 01:00:00 EEST+0300              -0.001
	          2 2024-05-27 23:00:00 EEST+0300 2024-05-28 01:00:00 EEST+0300               0.085
	          3 2024-05-27 22:00:00 EEST+0300 2024-05-28 01:00:00 EEST+0300            0.171667
	          4 2024-05-27 13:00:00 EEST+0300 2024-05-27 17:00:00 EEST+0300             0.20075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
