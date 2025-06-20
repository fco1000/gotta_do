from rest_framework import serializers
from journal.models import Journal

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = [
            "user_id",
            "date",
            "title",
            "content",
            "mood",
        ]