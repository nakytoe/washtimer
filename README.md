
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-01 10:00:00 EEST+0300 2024-07-01 11:00:00 EEST+0300                4.39
	          2 2024-07-01 09:00:00 EEST+0300 2024-07-01 11:00:00 EEST+0300               4.365
	          3 2024-07-01 09:00:00 EEST+0300 2024-07-01 12:00:00 EEST+0300            4.352667
	          4 2024-07-01 09:00:00 EEST+0300 2024-07-01 13:00:00 EEST+0300             4.32375

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-02 00:00:00 EEST+0300 2024-07-02 01:00:00 EEST+0300               3.809
	          2 2024-07-01 23:00:00 EEST+0300 2024-07-02 01:00:00 EEST+0300               3.868
	          3 2024-07-01 22:00:00 EEST+0300 2024-07-02 01:00:00 EEST+0300            3.928667
	          4 2024-07-01 21:00:00 EEST+0300 2024-07-02 01:00:00 EEST+0300             3.98375


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
