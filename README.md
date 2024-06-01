
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-02 20:00:00 EEST+0300 2024-06-02 21:00:00 EEST+0300              13.675
	          2 2024-06-02 19:00:00 EEST+0300 2024-06-02 21:00:00 EEST+0300              13.146
	          3 2024-06-02 19:00:00 EEST+0300 2024-06-02 22:00:00 EEST+0300           10.530333
	          4 2024-06-02 19:00:00 EEST+0300 2024-06-02 23:00:00 EEST+0300             10.4555

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-02 04:00:00 EEST+0300 2024-06-02 05:00:00 EEST+0300               0.123
	          2 2024-06-02 04:00:00 EEST+0300 2024-06-02 06:00:00 EEST+0300              0.1295
	          3 2024-06-02 03:00:00 EEST+0300 2024-06-02 06:00:00 EEST+0300            0.154667
	          4 2024-06-02 03:00:00 EEST+0300 2024-06-02 07:00:00 EEST+0300             0.18175


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
