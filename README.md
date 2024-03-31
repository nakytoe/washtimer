
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-03-31 20:00:00 EEST+0300 2024-03-31 21:00:00 EEST+0300               7.198
	          2 2024-03-31 19:00:00 EEST+0300 2024-03-31 21:00:00 EEST+0300              7.1715
	          3 2024-03-31 18:00:00 EEST+0300 2024-03-31 21:00:00 EEST+0300            6.957667
	          4 2024-03-31 18:00:00 EEST+0300 2024-03-31 22:00:00 EEST+0300               6.794

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-03-31 15:00:00 EEST+0300 2024-03-31 16:00:00 EEST+0300               3.804
	          2 2024-03-31 15:00:00 EEST+0300 2024-03-31 17:00:00 EEST+0300               3.923
	          3 2024-03-31 14:00:00 EEST+0300 2024-03-31 17:00:00 EEST+0300            3.983333
	          4 2024-03-31 13:00:00 EEST+0300 2024-03-31 17:00:00 EEST+0300             4.08675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
