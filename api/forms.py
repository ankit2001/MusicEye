from rest_framework import serializers
from api import models
from rest_framework.authentication import authenticate

# Creating developer profile forms
class DeveloperProfileForm(serializers.ModelSerializer):
    class Meta:
        model = models.DeveloperProfile
        # Adding fields
        fields = ('id', 'email', 'name', 'organisation', 'password')
        # Adding extra arguements
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password',
                }
            }
        }

    # Create the viewset
    
    def create(self, validated_data):
        developer_identity = models.DeveloperProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            organisation = validated_data['organisation'],
            password = validated_data['password']
        )
        return developer_identity


# Login token apis
class AccessTokenForm(serializers.Serializer):
    email = serializers.CharField()
    # Adding fields
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace = False
    )
    # Validation functions
    def validate(self, args):
        email = args.get('email')
        password = args.get('password')

        developer = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        # Non developer  cases
        if not developer:
            msg = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(msg, code = 'authorization')

        args['user'] = developer
        args['is_staff'] = developer.is_staff  
        return args

# Adding form for Music generation Viewset
class MusicReportForm(serializers.ModelSerializer):
    class Meta:
        # Adding model and fields
        model = models.MusicReportModel
        fields = ('id', 'developer_profile', 'parsed_text', 'timing','report', 'parsed_music')
        read_only_fields = ('developer_profile','report', 'parsed_music')
        """ extra_kwargs = {
            'report': {
                JSONField({}): True,
            }
        }
        """