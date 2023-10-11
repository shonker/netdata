<!--startmeta
custom_edit_url: "https://github.com/netdata/netdata/edit/master/collectors/charts.d.plugin/apcupsd/README.md"
meta_yaml: "https://github.com/netdata/netdata/edit/master/collectors/charts.d.plugin/apcupsd/metadata.yaml"
sidebar_label: "APC UPS"
learn_status: "Published"
learn_rel_path: "Data Collection/UPS"
message: "DO NOT EDIT THIS FILE DIRECTLY, IT IS GENERATED BY THE COLLECTOR'S metadata.yaml FILE"
endmeta-->

# APC UPS

Plugin: charts.d.plugin
Module: apcupsd

<img src="https://img.shields.io/badge/maintained%20by-Netdata-%2300ab44" />

## Overview

Monitor APC UPS performance with Netdata for optimal uninterruptible power supply operations. Enhance your power supply reliability with real-time APC UPS metrics.

The collector uses the `apcaccess` tool to contact the `apcupsd` daemon and get the APC UPS statistics.

This collector is supported on all platforms.

This collector only supports collecting metrics from a single instance of this integration.


### Default Behavior

#### Auto-Detection

By default, with no configuration provided, the collector will try to contact 127.0.0.1:3551 with using the `apcaccess` utility.

#### Limits

The default configuration for this integration does not impose any limits on data collection.

#### Performance Impact

The default configuration for this integration is not expected to impose a significant performance impact on the system.


## Metrics

Metrics grouped by *scope*.

The scope defines the instance that the metric belongs to. An instance is uniquely identified by a set of labels.



### Per ups

Metrics related to UPS. Each UPS provides its own set of the following metrics.

This scope has no labels.

Metrics:

| Metric | Dimensions | Unit |
|:------|:----------|:----|
| apcupsd.charge | charge | percentage |
| apcupsd.battery.voltage | voltage, nominal | Volts |
| apcupsd.input.voltage | voltage, min, max | Volts |
| apcupsd.output.voltage | absolute, nominal | Volts |
| apcupsd.input.frequency | frequency | Hz |
| apcupsd.load | load | percentage |
| apcupsd.load_usage | load | Watts |
| apcupsd.temperature | temp | Celsius |
| apcupsd.time | time | Minutes |
| apcupsd.online | online | boolean |



## Alerts


The following alerts are available:

| Alert name  | On metric | Description |
|:------------|:----------|:------------|
| [ apcupsd_ups_charge ](https://github.com/netdata/netdata/blob/master/health/health.d/apcupsd.conf) | apcupsd.charge | average UPS charge over the last minute |
| [ apcupsd_10min_ups_load ](https://github.com/netdata/netdata/blob/master/health/health.d/apcupsd.conf) | apcupsd.load | average UPS load over the last 10 minutes |
| [ apcupsd_last_collected_secs ](https://github.com/netdata/netdata/blob/master/health/health.d/apcupsd.conf) | apcupsd.load | number of seconds since the last successful data collection |


## Setup

### Prerequisites

#### Install charts.d plugin

If [using our official native DEB/RPM packages](https://github.com/netdata/netdata/blob/master/packaging/installer/UPDATE.md#determine-which-installation-method-you-used), make sure `netdata-plugin-chartsd` is installed.


#### Required software

Make sure the `apcaccess` and `apcupsd` are installed and running.


### Configuration

#### File

The configuration file name for this integration is `charts.d/apcupsd.conf`.


You can edit the configuration file using the `edit-config` script from the
Netdata [config directory](https://github.com/netdata/netdata/blob/master/docs/configure/nodes.md#the-netdata-config-directory).

```bash
cd /etc/netdata 2>/dev/null || cd /opt/netdata/etc/netdata
sudo ./edit-config charts.d/apcupsd.conf
```
#### Options

The config file is sourced by the charts.d plugin. It's a standard bash file.

The following collapsed table contains all the options that can be configured for the apcupsd collector.


<details><summary>Config options</summary>

| Name | Description | Default | Required |
|:----|:-----------|:-------|:--------:|
| apcupsd_sources | This is an array of apcupsd sources. You can have multiple entries there. Please refer to the example below on how to set it. | 127.0.0.1:3551 | False |
| apcupsd_timeout | How long to wait for apcupsd to respond. | 3 | False |
| apcupsd_update_every | The data collection frequency. If unset, will inherit the netdata update frequency. | 1 | False |
| apcupsd_priority | The charts priority on the dashboard. | 90000 | False |
| apcupsd_retries | The number of retries to do in case of failure before disabling the collector. | 10 | False |

</details>

#### Examples

##### Multiple apcupsd sources

Specify a multiple apcupsd sources along with a custom update interval

```yaml
# add all your APC UPSes in this array - uncomment it too
declare -A apcupsd_sources=(
    ["local"]="127.0.0.1:3551",
    ["remote"]="1.2.3.4:3551"
)

# how long to wait for apcupsd to respond
#apcupsd_timeout=3

# the data collection frequency
# if unset, will inherit the netdata update frequency
apcupsd_update_every=5

# the charts priority on the dashboard
#apcupsd_priority=90000

# the number of retries to do in case of failure
# before disabling the module
#apcupsd_retries=10

```


## Troubleshooting

### Debug Mode

To troubleshoot issues with the `apcupsd` collector, run the `charts.d.plugin` with the debug option enabled. The output
should give you clues as to why the collector isn't working.

- Navigate to the `plugins.d` directory, usually at `/usr/libexec/netdata/plugins.d/`. If that's not the case on
  your system, open `netdata.conf` and look for the `plugins` setting under `[directories]`.

  ```bash
  cd /usr/libexec/netdata/plugins.d/
  ```

- Switch to the `netdata` user.

  ```bash
  sudo -u netdata -s
  ```

- Run the `charts.d.plugin` to debug the collector:

  ```bash
  ./charts.d.plugin debug 1 apcupsd
  ```

