class Staff:
    def __init__(self, s_name, access_code):
        self.s_name = s_name
        self.__access_code = access_code

    @property
    def access_code(self):
        return self.__access_code

    @access_code.setter
    def access_code(self,new_code):
        if len(new_code)>= 6:
            self.__access_code = new_code
            print("Access code updated successfully.")
        else:
            print("Access code must be at least 6 characters long.")

    def display_info(self):
        print(f"Staff name: {self.s_name}")

    def view_access_code(self):
        print(f"Access code: {self.__access_code}")

staff1=Staff("Richard","UMaT 419")
staff1.display_info()
staff1.view_access_code()
staff1.access_code= "Admin456"
staff1.view_access_code()
staff1.access_code= "419"

