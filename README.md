
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-20 20:00:00 EEST+0300 2023-08-20 21:00:00 EEST+0300              31.005
	          2 2023-08-20 20:00:00 EEST+0300 2023-08-20 22:00:00 EEST+0300             27.9645
	          3 2023-08-20 20:00:00 EEST+0300 2023-08-20 23:00:00 EEST+0300           28.976667
	          4 2023-08-20 19:00:00 EEST+0300 2023-08-20 23:00:00 EEST+0300            27.92525

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-20 07:00:00 EEST+0300 2023-08-20 08:00:00 EEST+0300               3.848
	          2 2023-08-20 07:00:00 EEST+0300 2023-08-20 09:00:00 EEST+0300              6.5245
	          3 2023-08-20 07:00:00 EEST+0300 2023-08-20 10:00:00 EEST+0300            8.441333
	          4 2023-08-20 07:00:00 EEST+0300 2023-08-20 11:00:00 EEST+0300             9.43075


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
