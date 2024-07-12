
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-12 20:00:00 EEST+0300 2024-07-12 21:00:00 EEST+0300               3.691
	          2 2024-07-12 19:00:00 EEST+0300 2024-07-12 21:00:00 EEST+0300              3.6855
	          3 2024-07-12 18:00:00 EEST+0300 2024-07-12 21:00:00 EEST+0300            3.675667
	          4 2024-07-12 18:00:00 EEST+0300 2024-07-12 22:00:00 EEST+0300                3.67

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-13 00:00:00 EEST+0300 2024-07-13 01:00:00 EEST+0300               3.284
	          2 2024-07-12 23:00:00 EEST+0300 2024-07-13 01:00:00 EEST+0300              3.3685
	          3 2024-07-12 22:00:00 EEST+0300 2024-07-13 01:00:00 EEST+0300            3.423667
	          4 2024-07-12 14:00:00 EEST+0300 2024-07-12 18:00:00 EEST+0300               3.479


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
