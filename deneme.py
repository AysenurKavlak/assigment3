class multi():
    set_message: str = None
    set_count: int = 0
    set_display: str = None
    set_display: str = None
    def a(self):
        print(self.set_message, " ", self.set_count)

md = multi
md.set_message = "Hello World!"
md.set_count = 3
print(md.set_message, "Count:", md.set_count)
for i in range(3):
    print(md.set_message)
md.set_display = "Goodbye cruel world!"
for i in range(2):
    print(md.set_display)
print(md.set_display, "Count: 2" )
print("Current message:", md.set_display)