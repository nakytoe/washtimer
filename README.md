
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-17 08:00:00 EEST+0300 2023-08-17 09:00:00 EEST+0300               4.961
	          2 2023-08-17 07:00:00 EEST+0300 2023-08-17 09:00:00 EEST+0300              4.0975
	          3 2023-08-17 07:00:00 EEST+0300 2023-08-17 10:00:00 EEST+0300            3.495667
	          4 2023-08-17 07:00:00 EEST+0300 2023-08-17 11:00:00 EEST+0300             3.20575

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-08-17 01:00:00 EEST+0300 2023-08-17 02:00:00 EEST+0300               0.102
	          2 2023-08-17 01:00:00 EEST+0300 2023-08-17 03:00:00 EEST+0300                0.11
	          3 2023-08-17 01:00:00 EEST+0300 2023-08-17 04:00:00 EEST+0300            0.150667
	          4 2023-08-17 01:00:00 EEST+0300 2023-08-17 05:00:00 EEST+0300             0.18375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
