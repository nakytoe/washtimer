
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-31 12:00:00 EEST+0300 2023-08-31 13:00:00 EEST+0300              21.699
	          2 2023-08-31 12:00:00 EEST+0300 2023-08-31 14:00:00 EEST+0300              21.238
	          3 2023-08-31 11:00:00 EEST+0300 2023-08-31 14:00:00 EEST+0300           20.560333
	          4 2023-08-31 10:00:00 EEST+0300 2023-08-31 14:00:00 EEST+0300            19.78775

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-01 00:00:00 EEST+0300 2023-09-01 01:00:00 EEST+0300              11.663
	          2 2023-08-31 23:00:00 EEST+0300 2023-09-01 01:00:00 EEST+0300              12.279
	          3 2023-08-31 15:00:00 EEST+0300 2023-08-31 18:00:00 EEST+0300           13.295667
	          4 2023-08-31 14:00:00 EEST+0300 2023-08-31 18:00:00 EEST+0300             14.1195


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
