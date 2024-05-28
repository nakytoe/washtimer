
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-29 17:00:00 EEST+0300 2024-05-29 18:00:00 EEST+0300               30.99
	          2 2024-05-29 16:00:00 EEST+0300 2024-05-29 18:00:00 EEST+0300              27.895
	          3 2024-05-29 16:00:00 EEST+0300 2024-05-29 19:00:00 EEST+0300           20.783333
	          4 2024-05-29 16:00:00 EEST+0300 2024-05-29 20:00:00 EEST+0300            19.20375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-29 02:00:00 EEST+0300 2024-05-29 03:00:00 EEST+0300               0.098
	          2 2024-05-29 02:00:00 EEST+0300 2024-05-29 04:00:00 EEST+0300              0.1015
	          3 2024-05-29 01:00:00 EEST+0300 2024-05-29 04:00:00 EEST+0300            0.105667
	          4 2024-05-29 01:00:00 EEST+0300 2024-05-29 05:00:00 EEST+0300             0.11525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
