// int analogPin = A0;

int MIC0 = A0;     //analog input 0
int MIC1 = A1;     // analog input 1
int sig0 = 0; // Decalaramos una variable en la que volcaremos los datos que nos proporcione el sensor
int sig1 = 0;
int sig = 0;

void setup(){
  // Declaramos los led que tengamos como OUTPUT
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  // Declaramos el puerto del monitor serie
  Serial.begin(9600);
  while(!Serial){
  ;
  }
}

// Hacemos una función para controlar los LED
void led(int sig) {
  //sig = analogRead(MIC0); // Leemos lo que mide el sensor de sonido
  
  // Serial.println(sig); // Lo imprimimos por el monitor serie para ver que valores esta marcando el sensor
  // If para controlar los valores, si supera cierto valor, encendemos un pin
  // hay un if por cada led que hemos puesto cada uno tiene su valor para que se encienda.
  if (sig>20){ digitalWrite(2, HIGH);} else{ digitalWrite(2, LOW);}
  if (sig>70){ digitalWrite(3, HIGH);} else {digitalWrite(3, LOW);}
  if (sig>80){digitalWrite(4, HIGH);} else {digitalWrite(4, LOW);}
  if (sig>100){digitalWrite(5, HIGH);} else {digitalWrite(5, LOW);}
  if (sig>120){digitalWrite(6, HIGH);} else {digitalWrite(6, LOW);}
  }  
  

void loop(){
  sig0 = analogRead(MIC0);
  sig1 = analogRead(MIC1);
  sig = (sig0+sig1)/2;
  
  Serial.println(out);
  led(sig); // Llamamos a la función led
  delay(100);

}

void sendStatus(){
  char buffer[50];
  inputValue = analogRead(analogPin);
  sprintf(buffer, "Analog input %d is %d",analogPin,inputValue);
  Serial.println(buffer);
  
}
