import pytest
from sp_ask_school import (
    find_school_by_operator_suffix,
    find_queues_from_a_school_name,
    find_school_by_queue_or_profile_name,
    find_queue_by_criteria,
    sp_ask_school_dict
)

def test_find_school_by_operator_suffix():
    assert find_school_by_operator_suffix("nalini_tor") == "toronto"
    assert find_school_by_operator_suffix("librarian_west") == "Western"
    assert find_school_by_operator_suffix("user_mac") == "McMaster"
    assert find_school_by_operator_suffix(None) == None
    # Test cases for usernames without valid suffixes
    assert find_school_by_operator_suffix("novalidformat") == "Unknown"
    assert find_school_by_operator_suffix("guelph-librarian1") == "Guelph"
    assert find_school_by_operator_suffix("admin-toronto") == "admin"

def test_find_queues_from_a_school_name():
    toronto_queues = [
        "toronto",
        "toronto-mississauga",
        "toronto-scarborough",
        "toronto-st-george",
        "toronto-st-george-proactive",
    ]
    assert find_queues_from_a_school_name("Toronto") == toronto_queues
    assert find_queues_from_a_school_name("Invalid") == "Unknown"
    assert find_queues_from_a_school_name(None) == None

def test_find_school_by_queue_or_profile_name():
    assert find_school_by_queue_or_profile_name("western-proactive") == "Western"
    assert find_school_by_queue_or_profile_name("toronto-st-george") == "toronto"
    assert find_school_by_queue_or_profile_name("invalid-queue") == "Unknown"
    assert find_school_by_queue_or_profile_name(None) == None

def test_find_queue_by_criteria():
    french_queues = find_queue_by_criteria("-fr")
    assert "ottawa-fr" in french_queues
    assert "western-fr" in french_queues
    
    txt_queues = find_queue_by_criteria("-txt")
    assert "carleton-txt" in txt_queues
    assert "mcmaster-txt" in txt_queues
    
    # Test edge cases
    assert find_queue_by_criteria(None) == []
    assert find_queue_by_criteria("nonexistent") == []

def test_data_integrity():
    required_fields = ["id", "queues", "suffix", "short_name", "full_name"]
    for item in sp_ask_school_dict:
        school = item["school"]
        for field in required_fields:
            assert field in school, f"Missing field {field} in school {school.get('short_name', 'unknown')}"