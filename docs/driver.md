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

<a href="../sp110e/driver.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__()
```

Initialize object. 




---

<a href="../sp110e/driver.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../sp110e/driver.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect() → None
```

Close connection to device. 

---

<a href="../sp110e/driver.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ic_models`

```python
get_ic_models() → tuple
```

Get list of supported IC models. 

---

<a href="../sp110e/driver.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_modes`

```python
get_modes() → tuple
```

Get list of supported modes. 

---

<a href="../sp110e/driver.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_parameter`

```python
get_parameter(parameter: str) → Any
```

Get read parameter by name. 

---

<a href="../sp110e/driver.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_parameters`

```python
get_parameters() → dict
```

Get read parameters. 

---

<a href="../sp110e/driver.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_sequences`

```python
get_sequences() → tuple
```

Get list of supported RGB sequence types. 

---

<a href="../sp110e/driver.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_connected`

```python
is_connected() → bool
```

Check connection to device. 

---

<a href="../sp110e/driver.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_parameters`

```python
print_parameters()
```

Print device info. 

---

<a href="../sp110e/driver.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_parameters`

```python
read_parameters() → dict
```

Read parameters information from device. 

---

<a href="../sp110e/driver.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send_command`

```python
send_command(
    command_byte: <built-in function hex>,
    data_bytes: [<built-in function hex>, <built-in function hex>, <built-in function hex>] = (0, 0, 0)
)
```

Send command with data. 

---

<a href="../sp110e/driver.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../sp110e/driver.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write_parameters`

```python
write_parameters(parameters: dict, auto_read: bool = True) → Optional[dict]
```

Write device parameters to device in batch mode. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
