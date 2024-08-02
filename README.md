
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-02 20:00:00 EEST+0300 2024-08-02 21:00:00 EEST+0300               2.931
	          2 2024-08-02 19:00:00 EEST+0300 2024-08-02 21:00:00 EEST+0300              2.9245
	          3 2024-08-02 18:00:00 EEST+0300 2024-08-02 21:00:00 EEST+0300            2.915333
	          4 2024-08-02 18:00:00 EEST+0300 2024-08-02 22:00:00 EEST+0300                 2.9

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-08-02 07:00:00 EEST+0300 2024-08-02 08:00:00 EEST+0300               0.924
	          2 2024-08-02 07:00:00 EEST+0300 2024-08-02 09:00:00 EEST+0300              1.2415
	          3 2024-08-02 07:00:00 EEST+0300 2024-08-02 10:00:00 EEST+0300            1.571667
	          4 2024-08-02 07:00:00 EEST+0300 2024-08-02 11:00:00 EEST+0300               1.774


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
