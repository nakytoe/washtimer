
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-02 09:00:00 EEST+0300 2024-04-02 10:00:00 EEST+0300                6.95
	          2 2024-04-02 08:00:00 EEST+0300 2024-04-02 10:00:00 EEST+0300                6.63
	          3 2024-04-02 08:00:00 EEST+0300 2024-04-02 11:00:00 EEST+0300            6.355333
	          4 2024-04-02 07:00:00 EEST+0300 2024-04-02 11:00:00 EEST+0300               6.003

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-04-02 00:00:00 EEST+0300 2024-04-02 01:00:00 EEST+0300               0.041
	          2 2024-04-02 03:00:00 EEST+0300 2024-04-02 05:00:00 EEST+0300               0.089
	          3 2024-04-02 02:00:00 EEST+0300 2024-04-02 05:00:00 EEST+0300            0.112333
	          4 2024-04-02 02:00:00 EEST+0300 2024-04-02 06:00:00 EEST+0300               0.131


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
