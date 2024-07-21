
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-21 09:00:00 EEST+0300 2024-07-21 10:00:00 EEST+0300                2.92
	          2 2024-07-21 18:00:00 EEST+0300 2024-07-21 20:00:00 EEST+0300               2.867
	          3 2024-07-21 18:00:00 EEST+0300 2024-07-21 21:00:00 EEST+0300               2.854
	          4 2024-07-21 18:00:00 EEST+0300 2024-07-21 22:00:00 EEST+0300              2.8275

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-21 14:00:00 EEST+0300 2024-07-21 15:00:00 EEST+0300              -0.006
	          2 2024-07-21 13:00:00 EEST+0300 2024-07-21 15:00:00 EEST+0300              -0.002
	          3 2024-07-21 12:00:00 EEST+0300 2024-07-21 15:00:00 EEST+0300            0.024333
	          4 2024-07-21 12:00:00 EEST+0300 2024-07-21 16:00:00 EEST+0300             0.08125


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
