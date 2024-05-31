
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-31 08:00:00 EEST+0300 2024-05-31 09:00:00 EEST+0300              15.245
	          2 2024-05-31 08:00:00 EEST+0300 2024-05-31 10:00:00 EEST+0300              14.422
	          3 2024-05-31 08:00:00 EEST+0300 2024-05-31 11:00:00 EEST+0300           13.796667
	          4 2024-05-31 08:00:00 EEST+0300 2024-05-31 12:00:00 EEST+0300             13.1465

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-01 00:00:00 EEST+0300 2024-06-01 01:00:00 EEST+0300               0.956
	          2 2024-05-31 23:00:00 EEST+0300 2024-06-01 01:00:00 EEST+0300                1.25
	          3 2024-05-31 22:00:00 EEST+0300 2024-06-01 01:00:00 EEST+0300            1.586333
	          4 2024-05-31 21:00:00 EEST+0300 2024-06-01 01:00:00 EEST+0300               1.766


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
