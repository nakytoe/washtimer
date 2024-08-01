
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-01 16:00:00 EEST+0300 2024-08-01 17:00:00 EEST+0300               6.152
	          2 2024-08-01 16:00:00 EEST+0300 2024-08-01 18:00:00 EEST+0300              5.9665
	          3 2024-08-01 16:00:00 EEST+0300 2024-08-01 19:00:00 EEST+0300               5.208
	          4 2024-08-01 16:00:00 EEST+0300 2024-08-01 20:00:00 EEST+0300             4.94725

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-02 04:00:00 EEST+0300 2024-08-02 05:00:00 EEST+0300               0.326
	          2 2024-08-02 03:00:00 EEST+0300 2024-08-02 05:00:00 EEST+0300               0.331
	          3 2024-08-02 02:00:00 EEST+0300 2024-08-02 05:00:00 EEST+0300            0.359667
	          4 2024-08-02 02:00:00 EEST+0300 2024-08-02 06:00:00 EEST+0300              0.3795


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
