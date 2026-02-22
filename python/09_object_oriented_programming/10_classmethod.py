class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    @classmethod
    def from_str(cls,order_string):
        tea_type,sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)

order1 = ChaiOrder.from_dict({
    "tea_type":"masala",
    "sweetness":"medium",
    "size":"low"
})
order2 = ChaiOrder.from_str("Ginger-Low-Small")
print(order1.__dict__)
print(order2.__dict__)
