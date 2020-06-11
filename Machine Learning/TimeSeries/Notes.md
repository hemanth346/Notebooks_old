# Outliers :
 important to note diff bw anomaly vs extreme

To determine:
1. statistical - Z score
2. Clustering
3. Quartile based - IQR



Stationary series - no change in mean, SD, autocovariance
- examples used in ppt
  1. stationary
  2. increasing mean
  3. increasing SD
  4. chage in autocovariance

auto covariance
- relation between previous data and current data

  Trend stationary
  Difference Stationary

  > Can the trends by seasonal.?

Tests : unit root .?

Window types
  - Rolling - overlapping
  - Tumbling - no overlapping (will have data reduction by size of window)


ACF plot - seasonality behavior is captured
- Y axis : correlation
- X axis : lag/window size

Arima - forecasting :
Auto Regressive Integrated Moving Average


AR - pAcf
MA - Acf

to apply the model the series should be stationary, which will be done by the model; i.e integration

Box Jenkins model

LSTM - one of the best methods for TimeSeries

NN - No memory
RNN - have memory (feedback, very short term)
LSTM - have selective memory (has a forget layer)


activation fn. - model any linear into non-linear data
