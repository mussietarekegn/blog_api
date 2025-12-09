# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Post,Category

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','username','email']

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields=['id','name']

# class PostSerializer(serializers.ModelSerializer):
#     author=UserSerializer(read_only=True)
#     category=CategorySerializer()
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'author', 'category', 'created_at', 'updated_at']
#     def create(Self,validated_data):
#         category_data=validated_data.pop('category',None)
#         if category_data:
#             if category_data:
#                 cat, _ = Category.objects.get_or_create(name=category_data.get('name'))
#                 validated_data['category'] = cat
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         category_data = validated_data.pop('category', None)
#         if category_data:
#             cat, _ = Category.objects.get_or_create(name=category_data.get('name'))
#             instance.category = cat
#         return super().update(instance, validated_data)