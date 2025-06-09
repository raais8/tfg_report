class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"