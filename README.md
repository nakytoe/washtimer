
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-16 19:00:00 EEST+0300 2023-10-16 20:00:00 EEST+0300               7.097
	          2 2023-10-16 19:00:00 EEST+0300 2023-10-16 21:00:00 EEST+0300              5.0695
	          3 2023-10-16 19:00:00 EEST+0300 2023-10-16 22:00:00 EEST+0300            3.505667
	          4 2023-10-16 19:00:00 EEST+0300 2023-10-16 23:00:00 EEST+0300              2.7265

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-16 07:00:00 EEST+0300 2023-10-16 08:00:00 EEST+0300               0.017
	          2 2023-10-16 07:00:00 EEST+0300 2023-10-16 09:00:00 EEST+0300              0.0755
	          3 2023-10-16 07:00:00 EEST+0300 2023-10-16 10:00:00 EEST+0300            0.112667
	          4 2023-10-16 07:00:00 EEST+0300 2023-10-16 11:00:00 EEST+0300             0.14175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
