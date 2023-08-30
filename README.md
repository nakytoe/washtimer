
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-30 20:00:00 EEST+0300 2023-08-30 21:00:00 EEST+0300              22.599
	          2 2023-08-30 20:00:00 EEST+0300 2023-08-30 22:00:00 EEST+0300              21.721
	          3 2023-08-30 19:00:00 EEST+0300 2023-08-30 22:00:00 EEST+0300           20.436333
	          4 2023-08-30 18:00:00 EEST+0300 2023-08-30 22:00:00 EEST+0300             19.7655

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-31 00:00:00 EEST+0300 2023-08-31 01:00:00 EEST+0300              11.286
	          2 2023-08-30 23:00:00 EEST+0300 2023-08-31 01:00:00 EEST+0300             12.8735
	          3 2023-08-30 22:00:00 EEST+0300 2023-08-31 01:00:00 EEST+0300           14.137667
	          4 2023-08-30 21:00:00 EEST+0300 2023-08-31 01:00:00 EEST+0300              15.814


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
