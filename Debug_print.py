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
#Example
#TEST1
def TEST1():
    TEST_1 = 10
    TEST_2 = 40
    Debug('test_1', TEST_1)
    Debug('test_1C', TEST_1)
    Debug('test_2', TEST_2)
#main
def main():
    TEST1()
#start
main()