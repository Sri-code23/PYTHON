class animal():
    def sound(self) -> int:
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class bird(animal):
    def sound(self):
        print("birds sings")
object=bird()
object.sound()                       