
from algopy import ARC4Contract, String, UInt64
from algopy.arc4 import abimethod


class HelloWorld(ARC4Contract):
    # Global state
    greeting_count = UInt64()

    @abimethod()
    def hello(self, name: String) -> String:
        # Increment greeting count
        self.greeting_count.set(self.greeting_count.get() + 1)
        return "Hello, " + name

    @abimethod()
    def get_greeting_count(self) -> UInt64:
        return self.greeting_count.get()
