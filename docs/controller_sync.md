<!-- markdownlint-disable -->

<a href="../sp110e/controller_sync.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `controller_sync`






---

<a href="../sp110e/controller_sync.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ControllerSync`
Synchronous adapter for high-level sp110e asynchronous controller. 

Handy tool to use from Python shell or synchronous (normal) env. Inherits all synchronous methods from 'controller' class. 

Author: Pavel Roslovets https://roslovets.github.io 

<a href="../sp110e/controller_sync.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(mac_address: str = None, timeout: float = 3.0, retries: int = 0)
```

On object creation. 




---

<a href="../controller_sync/connect#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect()
```

Establish BLE connection to device. 

---

<a href="../controller_sync/disconnect#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect() → None
```

Close connection to device. 

---

<a href="../controller_sync/discover#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `discover`

```python
discover() → list
```

Discover BLE devices. 

---

<a href="../controller_sync/set_brightness#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_brightness`

```python
set_brightness(brightness: int, force: bool = False) → None
```

Set LED brightness (0-255). 

---

<a href="../controller_sync/set_color#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_color`

```python
set_color(
    color: [<class 'int'>, <class 'int'>, <class 'int'>],
    force: bool = False
) → None
```

Set static color in RGB format (0-255). 

---

<a href="../controller_sync/set_ic_model#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_ic_model`

```python
set_ic_model(ic_model: str, force: bool = False) → None
```

Set device IC model. 

---

<a href="../controller_sync/set_mode#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_mode`

```python
set_mode(mode: int, force: bool = False) → None
```

Set work mode (0-121). 0 - auto mode (demo). 

---

<a href="../controller_sync/set_pixels#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_pixels`

```python
set_pixels(pixels: int, force: bool = False) → None
```





---

<a href="../controller_sync/set_sequence#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_sequence`

```python
set_sequence(sequence: str, force: bool = False) → None
```

Set device color sequence. 

---

<a href="../controller_sync/set_speed#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_speed`

```python
set_speed(speed: int, force: bool = False) → None
```

Set speed of automatic modes (0-255). 

---

<a href="../controller_sync/set_white#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_white`

```python
set_white(white: int, force: bool = False) → None
```

Set brightness of white LED (0-255). 

---

<a href="../controller_sync/switch_off#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `switch_off`

```python
switch_off() → None
```

Switch device off. 

---

<a href="../controller_sync/switch_on#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `switch_on`

```python
switch_on() → None
```

Switch device on. 

---

<a href="../controller_sync/toggle#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `toggle`

```python
toggle() → bool
```

Toggle device state between on/off. 

---

<a href="../controller_sync/update#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update() → dict
```

Read device parameters. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
