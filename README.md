
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-21 18:00:00 EEST+0300 2023-10-21 19:00:00 EEST+0300               3.348
	          2 2023-10-21 17:00:00 EEST+0300 2023-10-21 19:00:00 EEST+0300              3.2235
	          3 2023-10-21 16:00:00 EEST+0300 2023-10-21 19:00:00 EEST+0300            3.251333
	          4 2023-10-21 16:00:00 EEST+0300 2023-10-21 20:00:00 EEST+0300              2.9035

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-21 07:00:00 EEST+0300 2023-10-21 08:00:00 EEST+0300               0.853
	          2 2023-10-21 07:00:00 EEST+0300 2023-10-21 09:00:00 EEST+0300              0.9545
	          3 2023-10-21 07:00:00 EEST+0300 2023-10-21 10:00:00 EEST+0300            1.020667
	          4 2023-10-21 07:00:00 EEST+0300 2023-10-21 11:00:00 EEST+0300             1.07525


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
