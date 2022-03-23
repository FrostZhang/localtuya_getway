# localtuya_getway

```diff
- 我只有一堆tuya的开关和一个可调亮度的灯（不能变色），所以别的设备可能会报错！！！！！！！！
```

原版localtuya仅支持wifi连接的tuya设备。我在 https://github.com/rospogrigio/localtuya 的基础上修改适配网关

不支持集成配置，请手动编辑yaml，注意在原版的上面增加了cid，这个是必须填的。

### zigbee网关 + zigbee设备
host 填网关的地址，device_id和local_key 不解释

entities里面的东西记住在cid填属于此设备cid，不同于device_id。
### wifi：
cid填device_id，其他不解释

网关下面的单位暂不知道怎么判定存在，默认都存在避免无法控制。

### 这是我的配置
```yaml
  - host: 192.168.2.26
    device_id: 000000000000
    local_key: abcdefghijklnm
    friendly_name: Tuya Getway
    protocol_version: "3.3"
    scan_interval: 30
    entities:
      - platform: switch
        friendly_name: tuyaSW1
        cid: 11111111111111
        id: 1
      - platform: switch
        friendly_name: tuyaSW2
        cid: 22222222222222
        id: 1
      - platform: light
        friendly_name: tuyaLT1
        cid: 33333333333333333
        id: 1
        brightness: 3
```
