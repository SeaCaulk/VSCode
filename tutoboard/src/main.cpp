#include <Arduino.h>

#define LED2 PC8
#define LED1 PB1
#define BUT1 PA0
#define BUT2 PA1
#define POT PB0
String msg;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED2,OUTPUT);
  pinMode(LED1,OUTPUT);
  pinMode(BUT2,INPUT_PULLDOWN);
  pinMode(BUT1,INPUT_PULLUP);
  pinMode(POT,INPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  // digitalWrite(LED2,HIGH);
  // digitalWrite(LED1,HIGH);
  // delay(500);

  // digitalWrite(LED1,LOW);
  // int etatBut2 = digitalRead(BUT2);
  // digitalWrite(LED2,etatBut2);
  // int etatBut1 = digitalRead(BUT1);
  // digitalWrite(LED1,etatBut1);
  // int valeurPot = analogRead(POT);
  // analogWrite(LED2,map(valeurPot,0,1023,0,255));
  // analogWrite(LED1,map(valeurPot,0,1023,255,0));
  // Serial.printf("avant : %d \t après : %d \n",valeurPot,map(valeurPot,0,1023,255,0));
  if (Serial.available()) // Vérifie s'il y a des données disponibles
{ 
    msg = Serial.readString();  // lit la valeur qu'on a envoyé et l'enregistre dans la variable msg
    Serial.println(msg);  //Affiche le texte contenu dans msg sur le moniteur
}
}

