from rest_framework import serializers
from .models import Introduction, AccountLinks, Projects, Timeline


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'


class AccountLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountLinks
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'