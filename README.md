
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-05 09:00:00 EEST+0300 2024-07-05 10:00:00 EEST+0300                3.68
	          2 2024-07-05 08:00:00 EEST+0300 2024-07-05 10:00:00 EEST+0300               3.619
	          3 2024-07-05 07:00:00 EEST+0300 2024-07-05 10:00:00 EEST+0300               3.239
	          4 2024-07-05 07:00:00 EEST+0300 2024-07-05 11:00:00 EEST+0300              3.0045

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-05 16:00:00 EEST+0300 2024-07-05 17:00:00 EEST+0300                 0.0
	          2 2024-07-05 15:00:00 EEST+0300 2024-07-05 17:00:00 EEST+0300              0.1015
	          3 2024-07-05 15:00:00 EEST+0300 2024-07-05 18:00:00 EEST+0300            0.147333
	          4 2024-07-05 14:00:00 EEST+0300 2024-07-05 18:00:00 EEST+0300             0.24825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
