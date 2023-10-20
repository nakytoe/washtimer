
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-20 11:00:00 EEST+0300 2023-10-20 12:00:00 EEST+0300               5.904
	          2 2023-10-20 11:00:00 EEST+0300 2023-10-20 13:00:00 EEST+0300              4.9175
	          3 2023-10-20 11:00:00 EEST+0300 2023-10-20 14:00:00 EEST+0300            4.518667
	          4 2023-10-20 10:00:00 EEST+0300 2023-10-20 14:00:00 EEST+0300              4.2325

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-21 00:00:00 EEST+0300 2023-10-21 01:00:00 EEST+0300               0.742
	          2 2023-10-20 23:00:00 EEST+0300 2023-10-21 01:00:00 EEST+0300               0.826
	          3 2023-10-20 22:00:00 EEST+0300 2023-10-21 01:00:00 EEST+0300               0.904
	          4 2023-10-20 21:00:00 EEST+0300 2023-10-21 01:00:00 EEST+0300               0.954


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
