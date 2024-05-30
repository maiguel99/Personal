import cv2

cascpath = "C:/Users/MIKI/Desktop/Python/GRAFICO/Reconocimiento Facial/haarcascade_frontalface_default.xml"#La ruta del archivo XML

faceCascade = cv2.CascadeClassifier(cascpath)#Carga el clasificador Haar para la deteccion de caras

video_capture = cv2.VideoCapture(0)#Inicia la captura de video desde la camara (la que haya como predeterminada del sistema)

while True:#Bucle

    ret, frame = video_capture.read()#Captura fotograma por fotograma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Convierte la imagen a escala de grises

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )#Deteccion de rostros en la imagen en escala de grises

    for (x, y, w, h) in faces:#Dibuja un rectángulo verde alrededor de la cara detectada
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow('Reconocimiento facial Snow White', frame)#Muestra el resultado de lo anterior

    if cv2.waitKey(1) & 0xFF == ord('q'):#Si se presiona la "q" durante 1 milisegunto se cierra el programa
        break

video_capture.release()#Libera el objeto de captura de video
cv2.destroyAllWindows()#Cierra la ventana de cv2