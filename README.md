
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-01 09:00:00 EEST+0300 2024-04-01 10:00:00 EEST+0300               5.254
	          2 2024-04-01 09:00:00 EEST+0300 2024-04-01 11:00:00 EEST+0300               5.161
	          3 2024-04-01 08:00:00 EEST+0300 2024-04-01 11:00:00 EEST+0300            5.104333
	          4 2024-04-01 08:00:00 EEST+0300 2024-04-01 12:00:00 EEST+0300              4.9905

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-02 00:00:00 EEST+0300 2024-04-02 01:00:00 EEST+0300               0.041
	          2 2024-04-01 23:00:00 EEST+0300 2024-04-02 01:00:00 EEST+0300              0.2785
	          3 2024-04-01 15:00:00 EEST+0300 2024-04-01 18:00:00 EEST+0300            0.769667
	          4 2024-04-01 15:00:00 EEST+0300 2024-04-01 19:00:00 EEST+0300               0.985


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
