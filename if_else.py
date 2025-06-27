class DrivingLicense:
    def get_DL(self,age):
        if 60 > age >=18:
            print("Eligible for Driving License")
        elif age < 18:
            print("Not Eligible for Driving License")
        elif 90 > age > 60:
            print("Eligible for Senior Citizen Driving License")
        elif age > 90:
            print("Ghar Baith")
        else:
            print("Invalid Age")


dl = DrivingLicense()
dl.get_DL(190)