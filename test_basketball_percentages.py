from basketball_percentages import calculate_season_predictions, calculate_shooting_percentage
    
import pytest
import random

shots_made = 4
shots_taken = 19

def test_calculate_season_predictions():
    season_predictions_list = []
    for item in "12345":
        season_predictions_list.append(random.randint(1, 15))
    return_list = calculate_season_predictions(season_predictions_list)
    assert return_list[0] == season_predictions_list[3] / season_predictions_list[0]
    assert return_list [1] == season_predictions_list[0] + season_predictions_list[1]
    assert return_list[2] == season_predictions_list[4] * return_list[1]
    assert return_list[3] == (return_list[2] - season_predictions_list[4]) / season_predictions_list[1]

def test_calculate_shooting_percentage():
    assert calculate_shooting_percentage(shots_made, shots_taken) == round(((shots_made / shots_taken) * 100), 2)

pytest.main(["-v", "--tb=line", "-rN", "test_basketball_percentages.py"])