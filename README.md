
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-22 09:00:00 EEST+0300 2024-05-22 10:00:00 EEST+0300               4.723
	          2 2024-05-22 08:00:00 EEST+0300 2024-05-22 10:00:00 EEST+0300              4.6215
	          3 2024-05-22 08:00:00 EEST+0300 2024-05-22 11:00:00 EEST+0300            4.456667
	          4 2024-05-22 07:00:00 EEST+0300 2024-05-22 11:00:00 EEST+0300              4.0855

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-23 00:00:00 EEST+0300 2024-05-23 01:00:00 EEST+0300                0.02
	          2 2024-05-22 23:00:00 EEST+0300 2024-05-23 01:00:00 EEST+0300               0.165
	          3 2024-05-22 22:00:00 EEST+0300 2024-05-23 01:00:00 EEST+0300            0.280333
	          4 2024-05-22 02:00:00 EEST+0300 2024-05-22 06:00:00 EEST+0300               0.333


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
