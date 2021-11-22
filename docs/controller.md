<!-- markdownlint-disable -->

<a href="../sp110e/controller.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `controller`






---

<a href="../sp110e/controller.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Controller`
High-level sp110e asynchronous controller. 

Use it only in asynchronous environment (with `asyncio`). 

Author: Pavel Roslovets https://roslovets.github.io 

<a href="../sp110e/controller.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(mac: str, timeout: float = 3.0, retries: int = 0)
```

On object creation. 




---

<a href="../sp110e/controller.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect()
```

Establish BLE connection to device. 

---

<a href="../sp110e/controller.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect() → None
```

Close connection to device. 

---

<a href="../sp110e/controller.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `discover`

```python
discover() → list
```

Discover BLE devices. 

---

<a href="../sp110e/controller.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_brightness`

```python
get_brightness() → int
```

Get LED brightness (0-255). 

---

<a href="../sp110e/controller.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_color`

```python
get_color() → [<class 'int'>, <class 'int'>, <class 'int'>]
```

Get static color in RGB format (0-255). 

---

<a href="../sp110e/controller.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ic_model`

```python
get_ic_model() → str
```

Get device IC model. 

---

<a href="../sp110e/controller.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ic_models`

```python
get_ic_models() → tuple
```

Get list of supported IC models. 

---

<a href="../sp110e/controller.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_mac_address`

```python
get_mac_address() → str
```

Get device MAC address. 

---

<a href="../sp110e/controller.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_mode`

```python
get_mode() → int
```

Get work mode (0-121). 0 - auto mode (demo). 

---

<a href="../sp110e/controller.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_modes`

```python
get_modes() → tuple
```

Get list of supported modes. 

---

<a href="../sp110e/controller.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_pixels`

```python
get_pixels() → int
```

Set number of pixels in LED strip. 

---

<a href="../sp110e/controller.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_sequence`

```python
get_sequence() → str
```

Set device color sequence. 

---

<a href="../sp110e/controller.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_sequences`

```python
get_sequences() → tuple
```

Get list of supported RGB sequence types. 

---

<a href="../sp110e/controller.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_speed`

```python
get_speed() → int
```

Get speed of automatic modes (0-255). 

---

<a href="../sp110e/controller.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_state`

```python
get_state() → bool
```

Get device state: on/off. 

---

<a href="../sp110e/controller.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_white`

```python
get_white() → int
```

Get brightness of white LED (0-255). 

---

<a href="../sp110e/controller.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_connected`

```python
is_connected()
```

Check device is connected. 

---

<a href="../sp110e/controller.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_on`

```python
is_on() → bool
```

Check device is On. 

---

<a href="../sp110e/controller.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_rgbw`

```python
is_rgbw() → bool
```

Check IC model supports RGBW mode. 

---

<a href="../sp110e/controller.py#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_parameters`

```python
print_parameters()
```

Print device info. 

---

<a href="../sp110e/controller.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_brightness`

```python
set_brightness(brightness: int, force: bool = False) → None
```

Set LED brightness (0-255). 

---

<a href="../sp110e/controller.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_color`

```python
set_color(
    color: [<class 'int'>, <class 'int'>, <class 'int'>],
    force: bool = False
) → None
```

Set static color in RGB format (0-255). 

---

<a href="../sp110e/controller.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_ic_model`

```python
set_ic_model(ic_model: str, force: bool = False) → None
```

Set device IC model. 

---

<a href="../sp110e/controller.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_mac_address`

```python
set_mac_address(mac_address: str) → None
```

Set device MAC address. 

---

<a href="../sp110e/controller.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_mode`

```python
set_mode(mode: int, force: bool = False) → None
```

Set work mode (0-121). 0 - auto mode (demo). 

---

<a href="../sp110e/controller.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_pixels`

```python
set_pixels(pixels: int, force: bool = False) → None
```

Set number of pixels in LED strip. 

---

<a href="../sp110e/controller.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_sequence`

```python
set_sequence(sequence: str, force: bool = False) → None
```

Set device color sequence. 

---

<a href="../sp110e/controller.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_speed`

```python
set_speed(speed: int, force: bool = False) → None
```

Set speed of automatic modes (0-255). 

---

<a href="../sp110e/controller.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_state`

```python
set_state(state: bool, force: bool = False) → None
```

Set device state: on/off. 

---

<a href="../sp110e/controller.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_white`

```python
set_white(white: int, force: bool = False) → None
```

Set brightness of white LED (0-255). 

---

<a href="../sp110e/controller.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `switch_off`

```python
switch_off() → None
```

Switch device off. 

---

<a href="../sp110e/controller.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `switch_on`

```python
switch_on() → None
```

Switch device on. 

---

<a href="../sp110e/controller.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `toggle`

```python
toggle() → bool
```

Toggle device state between on/off. 

---

<a href="../sp110e/controller.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update() → dict
```

Read device parameters. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
