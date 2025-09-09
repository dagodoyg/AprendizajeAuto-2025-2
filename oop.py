class method:
    def __init__(meth, name: str, field: str, accuracy: float ):
        meth.name = name
        meth.field = field
        meth.accuracy = accuracy
        print(f"{meth.name} succesfully indexed in {meth.field}")

    def resume(meth):
        return f"Field: {meth.field} \nMethod: {meth.name} \nAccuracy: {meth.accuracy}"

    def __del__(meth):
        print(f"{meth.name} in field {meth.field} unindexed")

method1 = method("method1", "physics", 0.01)
print(method1.resume())

del method1
