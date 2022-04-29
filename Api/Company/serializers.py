from rest_framework import serializers
from Api.Company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_email = serializers.EmailField(required=True, allow_null=False, allow_blank=False)
    company_manager_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_address = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    about_company = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_website = serializers.URLField(allow_blank=False, allow_null=False)

    class Meta:
        model = Company
        fields = ['id', 'company_name', 'company_email', 'company_manager_name', 'company_address', 'about_company',
                  'company_website']

    def create(self, validated_data):
        # try:
        company = Company.objects.create(**validated_data)
        company.save()
        return company
        # except Exception as e:
        #     return e


class CompanyUpdateSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_email = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_manager_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_address = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    about_company = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    company_website = serializers.URLField(allow_blank=False, allow_null=False)

    class Meta:
        model = Company
        fields = ['id', 'company_name', 'company_email', 'company_manager_name', 'company_address', 'about_company',
                  'company_website']

    def update(self, instance, validated_data):
        try:
            instance.company_name = validated_data.get('company_name', instance.company_name)
            instance.company_email = validated_data.get('company_email', instance.company_email)
            instance.company_manager_name = validated_data.get('company_manager_name', instance.company_manager_name)
            instance.company_address = validated_data.get('company_address', instance.company_address)
            instance.about_company = validated_data.get('about_company', instance.about_company)
            instance.company_website = validated_data.get('company_website', instance.company_website)
            instance.save()

            return instance
        except Exception as e:
            raise e


