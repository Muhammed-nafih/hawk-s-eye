# Importing all necessary libraries
import cv2
import os
from DBConnection import Db
import face_recognition
from email.mime import image
import os
import smtplib
from email.mime.text import MIMEText
staticpath=r"C:\Users\Mohammed Nafih\OneDrive\Desktop\hawks eye project\Thief_Detection\Thief\static\\"
urgmail="hawkseye486@gmail.com"
urpassword="hawkseye123"
cam = cv2.VideoCapture(1)
currentframe = 0
l=[]
falsecase=[]
identified = []
visit=[]
db = Db()
q = db.selectOne("select * from thief_camera")
camerauid=q['USER_id']

k = "Kannur"


def check(i,types,path):
    if types == 'criminal':
        # import required module
        from playsound import playsound

        # # for playing note.wav file
        # playsound(staticpath+'mixkit-residential-burglar-siren-1657.wav')
        # print('playing sound using playsound')

        # pip install pygame
        from pygame import mixer
        import time
        mixer.init()  # Initialzing pyamge mixer

        mixer.music.load(staticpath+'mixkit-residential-burglar-siren-1657.wav')  # Loading Music File

        mixer.music.play()  # Playing Music with Pygame

        time.sleep(5)

        mixer.music.stop()

        q1 = db.selectOne("select thief_user.*,thief_camera.id as cid,thief_camera.camera_number from thief_camera,thief_user where thief_camera.USER_id=thief_user.id and thief_camera.USER_id='" + str(
                camerauid) + "'")
        q3 = db.selectOne("select * from thief_criminals WHERE id='" + str(i) + "'")
        cname = q3['name']
        if q1 is not None:
            q2 = db.selectOne("select * from thief_alert where CAMERA_id='" + str(q['id']) + "' and date=curdate() and CRIMINALS_id='"+str(i)+"' ")
            if q2 is None:
                db.insert("insert into `thief_alert` values ( '',curdate(),'"+str(q['id'])+"','"+str(i)+"');")

                try:
                    gmail = smtplib.SMTP('smtp.gmail.com', 587)

                    gmail.ehlo()

                    gmail.starttls()

                    gmail.login(urgmail, urpassword)

                except Exception as e:
                    print("Couldn't setup email!!" + str(e))

                msg = MIMEText("Criminal "+cname)

                msg['Subject'] = 'Verification'

                msg['To'] = q1['email']

                msg['From'] = urgmail

                try:

                    gmail.send_message(msg)

                except Exception as e:

                    print("COULDN'T SEND EMAIL", str(e))

    if types == 'familear':
        db.insert("insert into thief_familiar_log values ('',curdate(),curtime(),'" + str(q['id'])+"','"+str(i)+"')")


while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name =  'a.jpg'
        print('Creating...' + name)
        import datetime
        ddd=datetime.datetime.now().strftime("%Y-%m-%d %H%M%S")
        cv2.imwrite(staticpath+"a.jpg", frame)
        cv2.imwrite(staticpath+ddd+".jpg", frame)
        # writing the extracted images
        path="/static/"+ddd+".jpg"
        from PIL import Image

        Original_Image = Image.open(staticpath + "a.jpg")

        rotated_image2 = Original_Image.transpose(Image.ROTATE_270)
        rotated_image2.save(staticpath + "a_270.jpg")

        qry = "select * from thief_criminals"
        db = Db()
        res = db.select(qry)
        if res is not None:
            print("Checking in criminal list")
            known_faces = []
            userids = []
            person_name = []

            # if res is not None:
            for result in res:
                try:
                    pic = result["photo"]
                    pname = pic.split("/")
                    img = staticpath + "photo\\" + pname[len(pname) - 1]
                    print(img)
                    b_img = face_recognition.load_image_file(img)
                    b_imgs = face_recognition.face_encodings(b_img)[0]
                    known_faces.append(b_imgs)
                    userids.append(result["id"])
                    person_name.append(result["name"])
                    print(str(len(known_faces)) + "done")
                except Exception as e:
                    print("eeeeeee",e)
                    pass


            unknown_image = face_recognition.load_image_file(staticpath + "a.jpg")
            unkonownpersons = face_recognition.face_encodings(unknown_image)
            if len(unkonownpersons) > 0:

                for i in range(0, len(unkonownpersons)):
                    h = unkonownpersons[i]

                    red = face_recognition.compare_faces(known_faces, h, tolerance=0.45)  # true,false,false,false]
                    print(red,"red")
                    for i in range(0, len(red)):
                        if red[i] == True:
                            check(userids[i],"criminal",path)
                            identified.append(userids[i])
                        else:
                            falsecase.append(userids[i])

        if len(res)==len(falsecase):
                falsecase.clear()
                identified.clear()
                print("Checking passed to familiar list")
                qry = "select * from thief_familiar_person WHERE thief_familiar_person.USER_id='"+str(camerauid)+"'"
                db = Db()
                res2 = db.select(qry)
                if res2 is not None:

                    known_faces = []
                    userids = []
                    person_name = []
                    identified = []
                    if res2 is not None:
                        for result in res2:
                            pic = result["F_image"]
                            pname = pic.split("/")
                            img = staticpath + "photo\\" +pname[len(pname) - 1]
                            print(img)
                            b_img = face_recognition.load_image_file(img)
                            b_imgs = face_recognition.face_encodings(b_img)[0]
                            known_faces.append(b_imgs)
                            userids.append(result["id"])
                            person_name.append(result["F_name"])
                            print(str(len(known_faces)) + "done")

                        unknown_image = face_recognition.load_image_file(staticpath + "a.jpg")
                        unkonownpersons = face_recognition.face_encodings(unknown_image)
                        print(len(unkonownpersons), "llllllllllllllllllllllll")
                        if len(unkonownpersons) > 0:

                            for i in range(0, len(unkonownpersons)):
                                h = unkonownpersons[i]

                                red = face_recognition.compare_faces(known_faces, h,
                                                                     tolerance=0.45)  # true,false,false,false]
                                print(red)
                                for i in range(0, len(red)):
                                    if red[i] == True:
                                        check(userids[i],"familear",path)
                                        identified.append(userids[i])
                                    else:
                                        print("hhhhhhhhhhhhhhhhhh")
                                        visit.append(userids[i])
                                        print(visit,"nnnnnnnnnnnnnnnnnnnnnnnn")
                print("kkkkkkkkkkkk",len(res2),visit)
                if len(res2)==len(visit):
                    visit.clear()
                    print("Visitor............")
                    db=Db()
                    db.insert("insert into thief_visitor_log(date,time,CAMERA_id,image) values (curdate(),curtime(),'"+str(q['id'])+"','"+path+"' )")
                    pass
        print("Loading Next frame")
        visit.clear()
        falsecase.clear()
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
print(l)

