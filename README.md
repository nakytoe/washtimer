
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-11 20:00:00 EEST+0300 2023-08-11 21:00:00 EEST+0300               2.923
	          2 2023-08-11 19:00:00 EEST+0300 2023-08-11 21:00:00 EEST+0300               2.878
	          3 2023-08-11 18:00:00 EEST+0300 2023-08-11 21:00:00 EEST+0300            2.741667
	          4 2023-08-11 18:00:00 EEST+0300 2023-08-11 22:00:00 EEST+0300              2.6625

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-12 06:00:00 EEST+0300 2023-08-12 07:00:00 EEST+0300                0.62
	          2 2023-08-12 06:00:00 EEST+0300 2023-08-12 08:00:00 EEST+0300               0.641
	          3 2023-08-12 05:00:00 EEST+0300 2023-08-12 08:00:00 EEST+0300            0.736667
	          4 2023-08-12 05:00:00 EEST+0300 2023-08-12 09:00:00 EEST+0300               0.802


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
