
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-30 20:00:00 EEST+0300 2023-08-30 21:00:00 EEST+0300              22.599
	          2 2023-08-30 20:00:00 EEST+0300 2023-08-30 22:00:00 EEST+0300              21.721
	          3 2023-08-31 11:00:00 EEST+0300 2023-08-31 14:00:00 EEST+0300           20.560333
	          4 2023-08-31 10:00:00 EEST+0300 2023-08-31 14:00:00 EEST+0300            19.78775

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-31 04:00:00 EEST+0300 2023-08-31 05:00:00 EEST+0300               4.257
	          2 2023-08-31 04:00:00 EEST+0300 2023-08-31 06:00:00 EEST+0300               4.322
	          3 2023-08-31 03:00:00 EEST+0300 2023-08-31 06:00:00 EEST+0300            4.365667
	          4 2023-08-31 02:00:00 EEST+0300 2023-08-31 06:00:00 EEST+0300             4.79225


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
