from rest_framework import serializers
from .models import Project, Pledge


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    #owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')
    def create(self, validated_data):
        return Project.objects.create(**validated_data)


    foodtypes = serializers.ChoiceField(choices=Project.CATEGORY_CHOICES)
    class Meta:
        Model = Project


    



class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()
#     
    
#     
    #user = serializers.ReadOnlyField(source='user.id')
    # project_id = serializers.ReadOnlyField(source='project.id')
    #data_created = serializers.ReadOnlyField()
    #type_id = serializers.IntegerField()



    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)




class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',
instance.is_open)
        instance.date_created = validated_data.get('date_created',
instance.date_created)
        instance.owner = validated_data.get('ownder',
instance.owner)
        instance.save()
        return instance



   