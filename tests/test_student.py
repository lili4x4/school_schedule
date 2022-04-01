from school_schedule.student import Student

def test_check_attributes_correctly_set():
    # arrange
    # ???

    # act
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ])

    # assert
    # assert student
    assert student.name == "Quinn"
    assert student.grade == "junior"
    assert student.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]

def test_add_class_adds_correct_class():
    #arrange
    student = Student(
            "Quinn", 
            "junior", 
            [
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition"
            ])
    #act
    updated_classes = student.add_class("Biology")

    #assert
    assert "Biology" in student.classes