import platform

if int(platform.python_version().split('.')[1]) < 11:
    from _dolphin_memory_engine import *
else:
    from dolphin_memory_engine._dolphin_memory_engine import (
        MemWatch,
        assert_hooked,
        follow_pointers,
        hook,
        is_hooked,
        read_byte,
        read_bytes,
        read_double,
        read_float,
        read_word,
        un_hook,
        write_byte,
        write_bytes,
        write_double,
        write_float,
        write_word,
    )

    __all__ = [
        "MemWatch",
        "assert_hooked",
        "follow_pointers",
        "hook",
        "un_hook",
        "is_hooked",
        "read_byte",
        "read_bytes",
        "read_double",
        "read_float",
        "read_word",
        "write_byte",
        "write_bytes",
        "write_double",
        "write_float",
        "write_word",
    ]

