from rest_framework import serializers
from .models import *


class LibraryReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReader
        fields = "__all__"
        read_only_fields = ["reader_id"]


class EducationStatsSerializer(serializers.Serializer):
    education_type = serializers.CharField(source='education')
    count = serializers.IntegerField()
    percentage = serializers.FloatField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["book_id"]


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = "__all__"


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


class ReaderHallHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderHallHistory
        fields = "__all__"


class ReaderCardHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderCardHistory
        fields = "__all__"


class BookMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMovement
        fields = "__all__"


class BookSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSet
        fields = "__all__"


class PerHallStatSerializer(serializers.Serializer):
    hall_number = serializers.IntegerField()
    hall_name = serializers.CharField()
    count = serializers.IntegerField()


class DailyEntityStatSerializer(serializers.Serializer):
    per_hall = PerHallStatSerializer(many=True)
    total = serializers.IntegerField()


class DailyReportSerializer(serializers.Serializer):
    date = serializers.DateField()
    books = DailyEntityStatSerializer()
    readers = DailyEntityStatSerializer()


class MonthlyRegistrationSerializer(serializers.Serializer):
    per_hall = PerHallStatSerializer(many=True)
    total = serializers.IntegerField()


class MonthlyLibraryReportSerializer(serializers.Serializer):
    period = serializers.CharField()
    daily_statistics = DailyReportSerializer(many=True)
    registrations = MonthlyRegistrationSerializer()


class EmployeesUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryEmployee
        fields = ['username']
