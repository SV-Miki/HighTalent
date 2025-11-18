from uuid import UUID

from rest_framework import serializers


def validate_non_empty_text(value: str, field_name: str = "Text") -> str:
    """
    Проверяет, что текст не пустой и не только пробелы.
    """
    if not value.strip():
        raise serializers.ValidationError(f"{field_name} cannot be empty")
    return value


def validate_uuid(value: str | UUID, field_name: str = "UUID") -> UUID:
    """
    Проверяет, что переданное значение является валидным UUID.
    """
    try:
        uuid_val = UUID(str(value))
    except ValueError:
        raise serializers.ValidationError(f"{field_name} must be a valid UUID")
    return uuid_val
