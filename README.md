
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-02 09:00:00 EEST+0300 2024-05-02 10:00:00 EEST+0300              49.343
	          2 2024-05-02 08:00:00 EEST+0300 2024-05-02 10:00:00 EEST+0300              46.371
	          3 2024-05-02 08:00:00 EEST+0300 2024-05-02 11:00:00 EEST+0300           41.265667
	          4 2024-05-02 07:00:00 EEST+0300 2024-05-02 11:00:00 EEST+0300            38.69925

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-05-01 16:00:00 EEST+0300 2024-05-01 17:00:00 EEST+0300               1.861
	          2 2024-05-01 16:00:00 EEST+0300 2024-05-01 18:00:00 EEST+0300               2.791
	          3 2024-05-01 16:00:00 EEST+0300 2024-05-01 19:00:00 EEST+0300               3.479
	          4 2024-05-01 16:00:00 EEST+0300 2024-05-01 20:00:00 EEST+0300               3.743


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
