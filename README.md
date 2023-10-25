
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-26 18:00:00 EEST+0300 2023-10-26 19:00:00 EEST+0300               9.839
	          2 2023-10-26 18:00:00 EEST+0300 2023-10-26 20:00:00 EEST+0300               9.634
	          3 2023-10-26 17:00:00 EEST+0300 2023-10-26 20:00:00 EEST+0300            9.372333
	          4 2023-10-26 16:00:00 EEST+0300 2023-10-26 20:00:00 EEST+0300             9.22375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-26 03:00:00 EEST+0300 2023-10-26 04:00:00 EEST+0300               2.296
	          2 2023-10-26 03:00:00 EEST+0300 2023-10-26 05:00:00 EEST+0300               2.302
	          3 2023-10-26 02:00:00 EEST+0300 2023-10-26 05:00:00 EEST+0300               2.328
	          4 2023-10-26 02:00:00 EEST+0300 2023-10-26 06:00:00 EEST+0300             2.36375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
