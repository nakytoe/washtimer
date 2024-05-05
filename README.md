
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-06 08:00:00 EEST+0300 2024-05-06 09:00:00 EEST+0300              16.152
	          2 2024-05-06 08:00:00 EEST+0300 2024-05-06 10:00:00 EEST+0300             14.3045
	          3 2024-05-06 08:00:00 EEST+0300 2024-05-06 11:00:00 EEST+0300           13.077333
	          4 2024-05-06 07:00:00 EEST+0300 2024-05-06 11:00:00 EEST+0300             12.4275

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-05 16:00:00 EEST+0300 2024-05-05 17:00:00 EEST+0300               0.529
	          2 2024-05-05 16:00:00 EEST+0300 2024-05-05 18:00:00 EEST+0300              0.5685
	          3 2024-05-05 16:00:00 EEST+0300 2024-05-05 19:00:00 EEST+0300            1.701667
	          4 2024-05-05 16:00:00 EEST+0300 2024-05-05 20:00:00 EEST+0300             2.44525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
