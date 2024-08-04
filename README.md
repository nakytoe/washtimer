
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-05 11:00:00 EEST+0300 2024-08-05 12:00:00 EEST+0300               3.462
	          2 2024-08-05 11:00:00 EEST+0300 2024-08-05 13:00:00 EEST+0300              3.4465
	          3 2024-08-05 10:00:00 EEST+0300 2024-08-05 13:00:00 EEST+0300            3.439333
	          4 2024-08-05 10:00:00 EEST+0300 2024-08-05 14:00:00 EEST+0300               3.435

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-04 16:00:00 EEST+0300 2024-08-04 17:00:00 EEST+0300               0.618
	          2 2024-08-04 16:00:00 EEST+0300 2024-08-04 18:00:00 EEST+0300              1.2915
	          3 2024-08-04 16:00:00 EEST+0300 2024-08-04 19:00:00 EEST+0300               1.767
	          4 2024-08-04 16:00:00 EEST+0300 2024-08-04 20:00:00 EEST+0300              2.1275


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
