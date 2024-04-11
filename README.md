
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-12 10:00:00 EEST+0300 2024-04-12 11:00:00 EEST+0300               8.133
	          2 2024-04-12 09:00:00 EEST+0300 2024-04-12 11:00:00 EEST+0300                8.04
	          3 2024-04-12 08:00:00 EEST+0300 2024-04-12 11:00:00 EEST+0300            7.311333
	          4 2024-04-12 08:00:00 EEST+0300 2024-04-12 12:00:00 EEST+0300              6.7905

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-12 00:00:00 EEST+0300 2024-04-12 01:00:00 EEST+0300               0.429
	          2 2024-04-12 00:00:00 EEST+0300 2024-04-12 02:00:00 EEST+0300              0.4725
	          3 2024-04-12 00:00:00 EEST+0300 2024-04-12 03:00:00 EEST+0300            0.486667
	          4 2024-04-12 00:00:00 EEST+0300 2024-04-12 04:00:00 EEST+0300              0.5005


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
