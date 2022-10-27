from rest_framework import serializers
from articles.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.email
    class Meta:
        model = Comment
        exclude = ("article", )
        
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)  # 하나만 넣어도 ,(콤마) 무조건!


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    # comment_set = CommentSerializer(many=True)  # related_name default = ~~~_set
    comments = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)  # 유저의 str 필드는 self.email로 설정 -> id가 아니라 이메일로 표시하기

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Article
        fields = '__all__'
        
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content")
        

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    class Meta:
        model = Article
        fields = ("pk", "title", "image", "updated_at", "user", "likes_count", "comments_count", )  