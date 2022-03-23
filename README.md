# localtuya_getway

原版localtuya仅支持wifi连接的tuya设备。我在 https://github.com/rospogrigio/localtuya 的基础上修改适配网关

不支持集成配置，请手动编辑yaml，注意在原版的上面增加了cid，这个是必须填的。

### zigbee网关 + zigbee设备
host 填网关的地址，device_id和local_key 不解释
entities里面的entitie记住在cid填属于此设备cid，不同于device_id。
### wifi：
cid填device_id，其他不解释

我只有一堆tuya的开关，所以别的设备可能会报错：

### 这是我的配置
```yaml
  - host: 192.168.2.26
    device_id: xxxxxxxxxxxx
    local_key: xxxxxxxxxxxxxx
    friendly_name: Tuya Getway
    protocol_version: "3.3"
    scan_interval: 30
    entities:
      - platform: switch
        friendly_name: tuyaSW1
        cid: xxxxxxxxxxx
        id: 1
        current: 18 # Optional
        current_consumption: 19 # Optional
        voltage: 20 # Optional
      - platform: switch
        friendly_name: tuyaSW2
        cid: xxxxxxxxxxx
        id: 1
        current: 18 # Optional
        current_consumption: 19 # Optional
        voltage: 20 # Optional
```
