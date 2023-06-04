from rest_framework import serializers


from todo_app.models import Item, TodoList


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "done"]
        read_only_fields = [
            "id",
        ]

    def create(self, validated_data, **kwargs):
        validated_data["todo_list_id"] = self.context["request"].parser_context["kwargs"]["pk"]

        if TodoList.objects.get(id=self.context["request"].parser_context["kwargs"]["pk"]).todo_items.filter(
            name=validated_data["name"]
        ):
            raise serializers.ValidationError("There's already this item on the list")

        return super(ItemSerializer, self).create(validated_data)


class TodoListSerializer(serializers.ModelSerializer):
    todo_items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ["id", "name", "todo_items"]
