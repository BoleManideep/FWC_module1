#include<Arduino.h>

int U=2, V=3, W=4, Z=5;
int F=9;

void setup() 
{
  pinMode(F, OUTPUT);
  pinMode(U, INPUT);
  pinMode(V, INPUT);
  pinMode(W, INPUT);
  pinMode(Z, INPUT);
}

void loop() 
{ 
  U=digitalRead(2);
  V=digitalRead(3);
  W=digitalRead(4);
  Z=digitalRead(5);
  
  F = (((U || !V) && !W) || Z);
  digitalWrite(9,F);
}
