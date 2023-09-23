
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-23 19:00:00 EEST+0300 2023-09-23 20:00:00 EEST+0300               0.856
	          2 2023-09-23 19:00:00 EEST+0300 2023-09-23 21:00:00 EEST+0300               0.808
	          3 2023-09-23 18:00:00 EEST+0300 2023-09-23 21:00:00 EEST+0300               0.785
	          4 2023-09-23 17:00:00 EEST+0300 2023-09-23 21:00:00 EEST+0300              0.7435

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-23 07:00:00 EEST+0300 2023-09-23 08:00:00 EEST+0300               0.029
	          2 2023-09-23 07:00:00 EEST+0300 2023-09-23 09:00:00 EEST+0300              0.0765
	          3 2023-09-23 07:00:00 EEST+0300 2023-09-23 10:00:00 EEST+0300            0.144333
	          4 2023-09-23 07:00:00 EEST+0300 2023-09-23 11:00:00 EEST+0300             0.20375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
