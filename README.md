
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-12 21:00:00 EEST+0300 2024-06-12 22:00:00 EEST+0300              19.188
	          2 2024-06-12 21:00:00 EEST+0300 2024-06-12 23:00:00 EEST+0300              19.085
	          3 2024-06-12 20:00:00 EEST+0300 2024-06-12 23:00:00 EEST+0300           18.510667
	          4 2024-06-12 20:00:00 EEST+0300 2024-06-13 00:00:00 EEST+0300            18.06675

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-12 03:00:00 EEST+0300 2024-06-12 04:00:00 EEST+0300               3.799
	          2 2024-06-12 03:00:00 EEST+0300 2024-06-12 05:00:00 EEST+0300               3.817
	          3 2024-06-12 03:00:00 EEST+0300 2024-06-12 06:00:00 EEST+0300            3.855667
	          4 2024-06-12 02:00:00 EEST+0300 2024-06-12 06:00:00 EEST+0300              3.8775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
