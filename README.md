
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-25 19:00:00 EEST+0300 2024-06-25 20:00:00 EEST+0300               4.392
	          2 2024-06-25 19:00:00 EEST+0300 2024-06-25 21:00:00 EEST+0300               4.387
	          3 2024-06-25 19:00:00 EEST+0300 2024-06-25 22:00:00 EEST+0300            4.372667
	          4 2024-06-25 18:00:00 EEST+0300 2024-06-25 22:00:00 EEST+0300              4.3495

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-25 16:00:00 EEST+0300 2024-06-25 17:00:00 EEST+0300               3.218
	          2 2024-06-25 16:00:00 EEST+0300 2024-06-25 18:00:00 EEST+0300              3.6525
	          3 2024-06-25 16:00:00 EEST+0300 2024-06-25 19:00:00 EEST+0300            3.861667
	          4 2024-06-25 16:00:00 EEST+0300 2024-06-25 20:00:00 EEST+0300             3.99425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
