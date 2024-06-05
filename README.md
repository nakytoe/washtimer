
# WashTimer

> Which hour to set the timer of your washing machine for cheapest wash? Look no further!

This page shows the periods for highest and lowest electricity prices in Finland 
for running home appliance programs of different lengths throughout the day. 

A GitHub Actions workflow updates the prices shown daily around 06:30 and 15:15 Europe/Helsinki time.

The max prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-05 08:00:00 EEST+0300 2024-06-05 09:00:00 EEST+0300              18.213
	          2 2024-06-05 08:00:00 EEST+0300 2024-06-05 10:00:00 EEST+0300             16.1825
	          3 2024-06-05 08:00:00 EEST+0300 2024-06-05 11:00:00 EEST+0300           13.061667
	          4 2024-06-05 08:00:00 EEST+0300 2024-06-05 12:00:00 EEST+0300            11.03625

The min prices for today:

	program [h]                    start time                      end time mean price [€c/kWh]
	          1 2024-06-05 17:00:00 EEST+0300 2024-06-05 18:00:00 EEST+0300               0.621
	          2 2024-06-05 16:00:00 EEST+0300 2024-06-05 18:00:00 EEST+0300               0.638
	          3 2024-06-05 16:00:00 EEST+0300 2024-06-05 19:00:00 EEST+0300               0.646
	          4 2024-06-05 15:00:00 EEST+0300 2024-06-05 19:00:00 EEST+0300               0.726


Source code available at [github.com/nakytoe/washtimer](https://github.com/nakytoe/washtimer).

Electricity prices retrieved from [porssisahko.net](https://porssisahko.net/api) open API.
