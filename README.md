
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-29 08:00:00 EEST+0300 2024-07-29 09:00:00 EEST+0300               4.006
	          2 2024-07-29 08:00:00 EEST+0300 2024-07-29 10:00:00 EEST+0300               3.765
	          3 2024-07-29 08:00:00 EEST+0300 2024-07-29 11:00:00 EEST+0300            3.635667
	          4 2024-07-29 07:00:00 EEST+0300 2024-07-29 11:00:00 EEST+0300              3.4175

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-29 16:00:00 EEST+0300 2024-07-29 17:00:00 EEST+0300              -0.004
	          2 2024-07-29 15:00:00 EEST+0300 2024-07-29 17:00:00 EEST+0300              -0.002
	          3 2024-07-29 14:00:00 EEST+0300 2024-07-29 17:00:00 EEST+0300              -0.001
	          4 2024-07-29 14:00:00 EEST+0300 2024-07-29 18:00:00 EEST+0300               0.153


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
