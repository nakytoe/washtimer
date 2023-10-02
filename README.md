
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-02 09:00:00 EEST+0300 2023-10-02 10:00:00 EEST+0300              40.909
	          2 2023-10-02 08:00:00 EEST+0300 2023-10-02 10:00:00 EEST+0300             33.2525
	          3 2023-10-02 08:00:00 EEST+0300 2023-10-02 11:00:00 EEST+0300           30.438333
	          4 2023-10-02 08:00:00 EEST+0300 2023-10-02 12:00:00 EEST+0300             28.4115

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2023-10-03 00:00:00 EEST+0300 2023-10-03 01:00:00 EEST+0300               0.384
	          2 2023-10-02 23:00:00 EEST+0300 2023-10-03 01:00:00 EEST+0300               0.451
	          3 2023-10-02 22:00:00 EEST+0300 2023-10-03 01:00:00 EEST+0300            0.507667
	          4 2023-10-02 21:00:00 EEST+0300 2023-10-03 01:00:00 EEST+0300             0.59425


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
