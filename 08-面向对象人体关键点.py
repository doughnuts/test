class Person:
    def __init__(self, landmarks,name, age):
        self.__landmarks = landmarks
        self.__name = name
        self.__age = age

    def add_landmark(self, landmark):
        if isinstance(landmark, LandMark):
            self.__landmarks.append(landmark)

    def show_landmarks(self):
        for landmark in self.__landmarks:
            print(landmark.landmark_id, landmark.x, landmark.y)



class LandMark:
    def __init__(self, landmark_id, x, y):
        self.landmark_id = landmark_id
        self.x = x
        self.y = y



landmark1 = LandMark(1, 100, 200)
landmark2 = LandMark(2, 300, 400)
landmark3 = LandMark(3, 500, 600)

person = Person([landmark1,landmark2,landmark3],"张三",20)
person.show_landmarks()