<!-- markdownlint-disable -->

<a href="../sp110e/driver.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `driver`





---

<a href="../sp110e/driver.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `discover`

```python
discover() → list
```

Discover BLE devices. 


---

<a href="../sp110e/driver.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Driver`
Low-level sp110e asynchronous BLE driver based on bleak library. 

Use it only if you know why. 

Author: Pavel Roslovets https://roslovets.github.io 

<a href="../sp110e/driver.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initialize object. 




---

<a href="../sp110e/driver.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect(
    mac_address: str,
    timeout: float = 3.0,
    auto_read: bool = True
) → Optional[dict]
```

Establish BLE connection to device. 

---

<a href="../sp110e/driver.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect() → None
```

Close connection to device. 

---

<a href="../sp110e/driver.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ic_models`

```python
get_ic_models() → tuple
```

Get list of supported IC models. 

---

<a href="../sp110e/driver.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_modes`

```python
get_modes() → tuple
```

Get list of supported modes. 

---

<a href="../sp110e/driver.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_parameter`

```python
get_parameter(parameter: str) → Any
```

Get read parameter by name. 

---

<a href="../sp110e/driver.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_parameters`

```python
get_parameters() → dict
```

Get read parameters. 

---

<a href="../sp110e/driver.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_sequences`

```python
get_sequences() → tuple
```

Get list of supported RGB sequence types. 

---

<a href="../sp110e/driver.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_connected`

```python
is_connected() → bool
```

Check connection to device. 

---

<a href="../sp110e/driver.py#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_ic_model_rgbw`

```python
is_ic_model_rgbw(ic_model: str = None) → bool
```

Check IC model supports RGBW mode. 

---

<a href="../sp110e/driver.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_parameters`

```python
print_parameters()
```

Print device info. 

---

<a href="../sp110e/driver.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_parameters`

```python
read_parameters() → dict
```

Read parameters information from device. 

---

<a href="../sp110e/driver.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_command`

```python
send_command(
    command_byte: <built-in function hex>,
    data_bytes: [<built-in function hex>, <built-in function hex>, <built-in function hex>] = (0, 0, 0)
)
```

Send command with data. 

---

<a href="../sp110e/driver.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write_parameter`

```python
write_parameter(
    parameter: str,
    value: Any,
    auto_read: bool = True
) → Optional[dict]
```

Write device parameter to device. 

---

<a href="../sp110e/driver.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write_parameters`

```python
write_parameters(parameters: dict, auto_read: bool = True) → Optional[dict]
```

Write device parameters to device in batch mode. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
