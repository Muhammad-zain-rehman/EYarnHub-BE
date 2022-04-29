from rest_framework import serializers
from Api.Company.models import Company
from Api.Post.models import Posts


class PostSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    author = serializers.SerializerMethodField(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    content = serializers.CharField()

    class Meta:
        model = Posts
        fields = ['id', 'title', 'author', 'author_id', 'content']

    def create(self, validated_data):
        author_request_id = validated_data.pop('author_id')
        validated_data['author'] = Company.objects.get(id=author_request_id)
        post = Posts.objects.create(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        author_request_id = validated_data.pop('author_id')
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)

        validated_data['author'] = Company.objects.get(id=author_request_id)
        instance.author = validated_data.get('author', instance.author)

        instance.save()
        return instance

    def get_author(self, obj):
        try:
            return obj.author.company_name
            # companyName = obj.Company.company_name
            # return companyName
        except Exception as e:
            raise




# class UpdatePostSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=255)
#     author = serializers.SerializerMethodField(read_only=True)
#     author_id = serializers.CharField(write_only=True)
#     content = serializers.CharField()
#
#     class Meta:
#         model = Posts
#         fields = ['title', 'author', 'author_id', 'content']


