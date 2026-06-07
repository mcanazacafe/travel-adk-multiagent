from travel_assistant.tools.culture_tools import get_local_culture_tips


def test_get_local_culture_tips_for_cusco():
    result = get_local_culture_tips("Cusco")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert len(result["typical_dishes"]) >= 1
    assert len(result["local_customs"]) >= 1
    assert len(result["useful_phrases"]) >= 1


def test_get_local_culture_tips_is_case_insensitive():
    result = get_local_culture_tips("  PARIS  ")

    assert result["status"] == "success"
    assert any("croissant" in dish.lower() for dish in result["typical_dishes"])


def test_get_local_culture_tips_unknown_destination():
    result = get_local_culture_tips("Ciudad Inventada")

    assert result["status"] == "not_found"
    assert "message" in result
