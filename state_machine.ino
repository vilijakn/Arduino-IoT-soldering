#define Off0 1
#define On1 6
#define On2 8
#define Off1 2
#define Off2 3

int  myStates=Off0, sampletimes=0; 

void setup() {

  pinMode(7, INPUT_PULLUP);
  pinMode(10, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  steit();
  delay(100);
}

void steit(){ 
 switch (myStates) {
     case Off0: if (digitalRead(7)==LOW){
      digitalWrite(10, 0), myStates=On1;
     }
     break;

     case On1: if (digitalRead(7)==HIGH){
  
      digitalWrite(10, 1), myStates=On2;
     } break;
     case On2: if (sampletimes>=4) {
               myStates = Off1, digitalWrite(10, 1);}
               else
               if (digitalRead(7)==LOW){
                myStates=Off2;
               }
               break;
  
     case Off1: if (sampletimes>=6){
                   myState = On2, digitalWrite(10, 0);}
                else
                if(digitalRead(7)==LOW){
                  myStates=Off2;
                }
                break;
                  

     case Off2: if(digitalRead(7)==HIGH){
                myStates=Off0, digitalWrite(10,0); 
                }
                break;
     
     default: myStates=Off0;
}
}

}
