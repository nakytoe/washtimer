
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-02 21:00:00 EEST+0300 2023-09-02 22:00:00 EEST+0300              16.499
	          2 2023-09-02 20:00:00 EEST+0300 2023-09-02 22:00:00 EEST+0300              16.155
	          3 2023-09-02 20:00:00 EEST+0300 2023-09-02 23:00:00 EEST+0300           15.537333
	          4 2023-09-02 19:00:00 EEST+0300 2023-09-02 23:00:00 EEST+0300              15.063

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-09-03 00:00:00 EEST+0300 2023-09-03 01:00:00 EEST+0300               6.407
	          2 2023-09-02 16:00:00 EEST+0300 2023-09-02 18:00:00 EEST+0300              9.2635
	          3 2023-09-02 16:00:00 EEST+0300 2023-09-02 19:00:00 EEST+0300              10.929
	          4 2023-09-02 16:00:00 EEST+0300 2023-09-02 20:00:00 EEST+0300            11.60675


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
