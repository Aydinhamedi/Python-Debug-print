# Python Debug print

This function is used for debugging purposes. It prints out various information about the data passed to it.

>  **Note**\
>  Please note that this code uses my print_color\
>  for more info go to https://github.com/Aydinhamedi/Python-color-print.

## Installation

No installation is required for this function. Simply copy the code and use it in your project.

## Usage

```python
#pylibs
import inspect
import traceback
from datetime import datetime
from PrintColor.Print_color import print_Color
#global Var
Debug_m = True
#Debug
def Debug(ID, DEBUG_IF, SFL: bool = True, Force: bool = False, SFCS: bool = True):
    """
    This function is used for debugging purposes. It prints out various information about the data passed to it.

    Args:
        ID (Any): The identifier for the data. This could be any type, but is typically a string.
        DEBUG_IF (Any): The data that needs to be debugged. This could be any type.
        SFL (bool, optional): A flag to determine if the stack frame location should be included in the debug information. Defaults to True.
        Force (bool, optional): A flag to force the debug information to be printed even if the global Debug_m is set to False. Defaults to False.
        SFCS (bool, optional): A flag to determine if the function call stack should be included in the debug information. Defaults to True.

    Returns:
        None
    """
    try:
        if Debug_m or Force:
            frame_info = inspect.currentframe()
            stack_trace = traceback.format_stack()
            stack_trace_formated = ''
            for line in stack_trace[:-1]:
                stack_trace_formated += '--> [!>>>' + line 
            location = f'{inspect.stack()[1].filename}:{frame_info.f_back.f_lineno}' if SFL else f'L:{frame_info.f_back.f_lineno}'
            Debug_data = \
            f'\n~*--> ~*DEBUG INFO id: ~*[{str(ID)}]~*, ' \
            f'Location: ~*[{location}]~*, ' \
            f'time: ~*[{datetime.now().strftime("%Y/%m/%d | %H:%M:%S")}]\n~*--> ~*' \
            f'Data: ~*{str(DEBUG_IF)}\n~*--> ~*' \
            f'Data Type: ~*{type(DEBUG_IF)}\n~*--> ~*' \
            f'Memory Address: ~*DEC>>>~*{id(DEBUG_IF)}~* | HEX>>>~*{hex(id(DEBUG_IF))}~* | BIN>>>~*{bin(id(DEBUG_IF))}\n' 
            if SFCS:
                Debug_data += f'~*--> ~*Function Call Stack: ~*↓\n~*{stack_trace_formated}\n'
            print_Color(Debug_data,
            ['red', 'magenta', 'green', 'magenta', 'yellow', 'magenta', 'yellow',
            'red', 'magenta', 'yellow', 'red', 'magenta', 'yellow', 'red', 'magenta',
            'cyan', 'yellow', 'cyan', 'yellow', 'cyan', 'yellow', 'red', 'magenta', 'green', 'yellow'] if SFCS else \
            ['red', 'magenta', 'green', 'magenta', 'yellow', 'magenta', 'yellow',
            'red', 'magenta', 'yellow', 'red', 'magenta', 'yellow', 'red', 'magenta',
            'cyan', 'yellow', 'cyan', 'yellow', 'cyan', 'yellow'], 
            advanced_mode=True)
    except NameError:
        print_Color('~*[`Debug` func] --> ERROR: ~*carate a global var named `Debug_m` for turning on and off the Debug func.', ['red', 'yellow'], advanced_mode=True)
# Example usage
Debug("data_id", data_to_debug)
```

## Arguments

- `ID`: The identifier for the data. This could be any type, but is typically a string.
- `DEBUG_IF`: The data that needs to be debugged. This could be any type.
- `SFL` (optional): A flag to determine if the stack frame location should be included in the debug information. Defaults to True.
- `Force` (optional): A flag to force the debug information to be printed even if the global `Debug_m` is set to False. Defaults to False.
- `SFCS` (optional): A flag to determine if the function call stack should be included in the debug information. Defaults to True.

## Output

The `Debug` function will print out the following information:

- Debug information ID, location, and timestamp
- Data value and data type
- Memory address in decimal, hexadecimal, and binary format
- Function call stack (if `SFCS` flag is set to True)

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).
