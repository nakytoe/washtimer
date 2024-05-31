
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-31 19:00:00 EEST+0300 2024-05-31 20:00:00 EEST+0300              12.954
	          2 2024-05-31 19:00:00 EEST+0300 2024-05-31 21:00:00 EEST+0300              12.581
	          3 2024-05-31 18:00:00 EEST+0300 2024-05-31 21:00:00 EEST+0300           11.721667
	          4 2024-05-31 17:00:00 EEST+0300 2024-05-31 21:00:00 EEST+0300            11.02275

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-01 00:00:00 EEST+0300 2024-06-01 01:00:00 EEST+0300               0.956
	          2 2024-05-31 23:00:00 EEST+0300 2024-06-01 01:00:00 EEST+0300                1.25
	          3 2024-05-31 23:00:00 EEST+0300 2024-06-01 02:00:00 EEST+0300               1.474
	          4 2024-05-31 23:00:00 EEST+0300 2024-06-01 03:00:00 EEST+0300               1.574


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
