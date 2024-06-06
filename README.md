
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-06 09:00:00 EEST+0300 2024-06-06 10:00:00 EEST+0300               7.441
	          2 2024-06-06 08:00:00 EEST+0300 2024-06-06 10:00:00 EEST+0300              6.6995
	          3 2024-06-06 08:00:00 EEST+0300 2024-06-06 11:00:00 EEST+0300            6.326667
	          4 2024-06-06 08:00:00 EEST+0300 2024-06-06 12:00:00 EEST+0300               5.765

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-07 00:00:00 EEST+0300 2024-06-07 01:00:00 EEST+0300               1.544
	          2 2024-06-06 14:00:00 EEST+0300 2024-06-06 16:00:00 EEST+0300              1.5625
	          3 2024-06-06 14:00:00 EEST+0300 2024-06-06 17:00:00 EEST+0300            1.582667
	          4 2024-06-06 13:00:00 EEST+0300 2024-06-06 17:00:00 EEST+0300             1.61725


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
