
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-03 18:00:00 EEST+0300 2023-08-03 19:00:00 EEST+0300               3.951
	          2 2023-08-03 18:00:00 EEST+0300 2023-08-03 20:00:00 EEST+0300               3.931
	          3 2023-08-03 18:00:00 EEST+0300 2023-08-03 21:00:00 EEST+0300            3.920667
	          4 2023-08-03 18:00:00 EEST+0300 2023-08-03 22:00:00 EEST+0300             3.87575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-03 15:00:00 EEST+0300 2023-08-03 16:00:00 EEST+0300                2.23
	          2 2023-08-03 15:00:00 EEST+0300 2023-08-03 17:00:00 EEST+0300               2.247
	          3 2023-08-03 14:00:00 EEST+0300 2023-08-03 17:00:00 EEST+0300            2.397667
	          4 2023-08-03 14:00:00 EEST+0300 2023-08-03 18:00:00 EEST+0300              2.6025


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
