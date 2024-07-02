
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-03 11:00:00 EEST+0300 2024-07-03 12:00:00 EEST+0300               4.874
	          2 2024-07-03 11:00:00 EEST+0300 2024-07-03 13:00:00 EEST+0300              4.8625
	          3 2024-07-03 11:00:00 EEST+0300 2024-07-03 14:00:00 EEST+0300            4.811667
	          4 2024-07-03 11:00:00 EEST+0300 2024-07-03 15:00:00 EEST+0300             4.80225

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-03 01:00:00 EEST+0300 2024-07-03 02:00:00 EEST+0300               0.461
	          2 2024-07-03 01:00:00 EEST+0300 2024-07-03 03:00:00 EEST+0300               1.214
	          3 2024-07-03 01:00:00 EEST+0300 2024-07-03 04:00:00 EEST+0300            1.762333
	          4 2024-07-03 01:00:00 EEST+0300 2024-07-03 05:00:00 EEST+0300              2.0875


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
