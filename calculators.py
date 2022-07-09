# Some high tech AI stuffs right here
import random

def _bmr_calculate(user_data):
    ### BMR
    # Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
    # Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)

    if user_data.sex == "Male":
        BMR = 88.362 + (13.397*user_data.weight) + \
        (4.799*user_data.height) - (5.677*user_data.age)
    else:
        BMR = 447.593 + (9.247*user_data.weight) + \
        (3.098*user_data.height) - (4.330*user_data.age)

    return BMR

def _tdee_calculate(user_data):
    ### TDEE (daily caloric intake)
    # Sedentary (little or no exercise): calories = BMR × 1.2;
    # Lightly active 
    # (light exercise/sports 1-3 days/week): calories = BMR × 1.375;
    # Moderately active 
    # (moderate exercise/sports 3-5 days/week): calories = BMR × 1.55;
    # Very active 
    # (hard exercise/sports 6-7 days a week): calories = BMR × 1.725; and
    # Extremely active 
    # (very hard exercise/sports & a physical job): calories = BMR × 1.9.
    
    calories = _bmr_calculate(user_data)*user_data.excercising_factor
    
    return calories

def _macro_in_grams(total_calo):
    carb_calo =  total_calo*random.randint(0.45,0.65)/100
    protein_calo = total_calo*random.randint(20,35)/100
    fat_calo = total_calo - carb_calo - protein_calo
    return {
        "carb":int(carb_calo/4),
        "protein":int(protein_calo/4),
        "fat":int(fat_calo/9),
        "total_calories": total_calo
        }

def _macro_per_meal(user_data):
    
    breakfast_calo_ratio = 0.3
    lunch_calo_ratio = 0.4
    dinner_calo_ratio = 0.3
    
    tdee_index = _tdee_calculate(user_data)
    breakfast_calo = tdee_index*breakfast_calo_ratio
    lunch_calo = tdee_index*lunch_calo_ratio
    dinner_calo = tdee_index*dinner_calo_ratio

    _brkfast = _macro_in_grams(breakfast_calo)
    _lunch   = _macro_in_grams(lunch_calo)
    _dinner  = _macro_in_grams(dinner_calo)
    
    return {
        "breakfast":_brkfast,
        "lunch":_lunch,
        "dinner": _dinner,
    }

def test_run():

    # code = 1
    # test_user_data = json.load(open("test_user_data.json", 'r'))
    
    # try:
    #     BMR = _bmr_calculate(test_user_data)
    # except Exception as e:
    #     code = 0
    #     mess = "BMR bug"

    # try:
    #     TDEE = _tdee_calculate(test_user_data)
    # except Exception as e:
    #     code = 0
    #     mess = "TDEE bug" 

    return 1, "Unimplemented health check API"