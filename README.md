
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-02 09:00:00 EEST+0300 2024-07-02 10:00:00 EEST+0300               3.768
	          2 2024-07-02 08:00:00 EEST+0300 2024-07-02 10:00:00 EEST+0300                3.76
	          3 2024-07-02 08:00:00 EEST+0300 2024-07-02 11:00:00 EEST+0300               3.699
	          4 2024-07-02 08:00:00 EEST+0300 2024-07-02 12:00:00 EEST+0300              3.6615

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-07-02 17:00:00 EEST+0300 2024-07-02 18:00:00 EEST+0300               3.019
	          2 2024-07-02 16:00:00 EEST+0300 2024-07-02 18:00:00 EEST+0300               3.124
	          3 2024-07-02 16:00:00 EEST+0300 2024-07-02 19:00:00 EEST+0300            3.178333
	          4 2024-07-02 16:00:00 EEST+0300 2024-07-02 20:00:00 EEST+0300               3.226


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
