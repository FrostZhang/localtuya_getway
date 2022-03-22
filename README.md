# localtuya_getway
项目尚未完工
原版localtuya仅支持wifi连接的tuya设备。我在 https://github.com/rospogrigio/localtuya 的基础上修改适配网关

不支持集成配置，请手动编辑yaml

配置开关：

```yaml
localtuya:
  - host: 192.168.1.x
    device_id: xxxxx
    local_key: xxxxx
    friendly_name: Tuya Device
    protocol_version: "3.3"
    scan_interval: # optional, only needed if energy monitoring values are not updating
      seconds: 30 # Values less than 10 seconds may cause stability issues
    entities:
      - platform: binary_sensor
        friendly_name: Plug Status
        id: 1
        device_class: power
        state_on: "true" # Optional
        state_off: "false" # Optional
      - platform: switch
        cid: xxxxxxxxxxx
        friendly_name: Plug
        id: 1
        current: 18 # Optional
        current_consumption: 19 # Optional
        voltage: 20 # Optional
```
