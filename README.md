
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-28 19:00:00 EEST+0300 2023-10-28 20:00:00 EEST+0300              18.028
	          2 2023-10-28 18:00:00 EEST+0300 2023-10-28 20:00:00 EEST+0300              17.074
	          3 2023-10-27 18:00:00 EEST+0300 2023-10-27 21:00:00 EEST+0300           15.593333
	          4 2023-10-27 17:00:00 EEST+0300 2023-10-27 21:00:00 EEST+0300            14.44375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-28 04:00:00 EEST+0300 2023-10-28 05:00:00 EEST+0300               4.266
	          2 2023-10-28 03:00:00 EEST+0300 2023-10-28 05:00:00 EEST+0300              4.3125
	          3 2023-10-28 03:00:00 EEST+0300 2023-10-28 06:00:00 EEST+0300            4.337333
	          4 2023-10-28 02:00:00 EEST+0300 2023-10-28 06:00:00 EEST+0300             4.37825


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
