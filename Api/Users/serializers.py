from rest_framework import serializers
from Api.Users.models import User, Role


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=True)
    email = serializers.EmailField(required=True)
    image = serializers.ImageField(required=True, allow_null=True, allow_empty_file=True)
    user_role = serializers.SerializerMethodField(read_only=True)
    role_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'is_active', 'email', 'image', 'user_role', 'role_code']

    def create(self, validated_data):
        requested_user_role = validated_data.pop('role_code')
        validated_data['user_role'] = Role.objects.get(code=requested_user_role)
        user = User.objects.create(**validated_data)
        user.save()
        return user

    def get_user_role(self, obj):
        try:
            obj.Role.name
        except:
            None


class UserUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=True)
    email = serializers.EmailField(required=True)
    image = serializers.ImageField(required=True, allow_null=True, allow_empty_file=True)
    user_role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'is_active', 'email', 'image', 'user_role']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.email = validated_data.get('email', instance.email)
        if "image" in validated_data.keys():
            image = validated_data.pop("image")
            validated_data["image"] = image
            instance.image = validated_data.get('image', instance.image)
        if "user_role" in validated_data.keys():
            requested_user_role = validated_data.pop("user_role")
            validated_data["user_role"] = Role.objects.get(code=requested_user_role)
            instance.user_role = validated_data.get("user_roel", instance.user_role)

        instance.save()
        return instance

        instance.save()

        return instance
