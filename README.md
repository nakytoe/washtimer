
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-01 19:00:00 EEST+0300 2024-06-01 20:00:00 EEST+0300               5.441
	          2 2024-06-01 19:00:00 EEST+0300 2024-06-01 21:00:00 EEST+0300               5.201
	          3 2024-06-01 18:00:00 EEST+0300 2024-06-01 21:00:00 EEST+0300            4.958667
	          4 2024-06-01 18:00:00 EEST+0300 2024-06-01 22:00:00 EEST+0300              4.3885

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-02 00:00:00 EEST+0300 2024-06-02 01:00:00 EEST+0300               1.427
	          2 2024-06-01 23:00:00 EEST+0300 2024-06-02 01:00:00 EEST+0300              1.8545
	          3 2024-06-01 07:00:00 EEST+0300 2024-06-01 10:00:00 EEST+0300               2.216
	          4 2024-06-01 07:00:00 EEST+0300 2024-06-01 11:00:00 EEST+0300             2.35775


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
