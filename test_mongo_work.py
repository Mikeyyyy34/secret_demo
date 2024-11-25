def test_add_patient():
    from mongo_work import add_patient
    new_patient = add_patient(102, "Ernie")
    answer = new_patient.save()
    assert answer.id == 102
