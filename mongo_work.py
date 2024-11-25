from pymodm import connect, MongoModel, fields
import os

m_pswd = os.environ.get("MONGODB")
m_id = os.environ.get("MONGODB_ID")

connect("mongodb+srv://{}:{}@cluster0.dvqkx.mongodb.net/".format(m_id, m_pswd)
        + "bme547?retryWrites=true&w=majority&appName=Cluster0")


class Patient(MongoModel):
    id = fields.IntegerField()
    name = fields.CharField()


def add_patient(mrn, name):
    new_patient = Patient(id=mrn, name=name)
    answer = new_patient.save()
    print(answer)
    return answer


if __name__ == "__main__":
    add_patient(105, "David")
