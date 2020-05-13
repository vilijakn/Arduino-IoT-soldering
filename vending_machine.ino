#define S0 1
#define S5 2
#define S10 3
#define S15 5
#define S20 33

#define on 78
#define off 36

#define Off0 777
#define On1 6
#define On2 8
#define Off1 95
#define Off2 63


int n=0, d=0, error =off, R, C, myState=S0, myStates=Off0, sampletimes=0, sampletime=0; 

void setup() {
  
  pinMode(2, INPUT_PULLUP);//nickel
  pinMode(3, INPUT_PULLUP);//dime
  pinMode(12, OUTPUT);//Release Item
  pinMode(13, OUTPUT);//Release change (a nickel)

  
  pinMode(7, INPUT_PULLUP);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

void loop() {
 machine();
 steit();
 delay(100);

}

void machine(){ 
Determine_n_d(); 
 
 switch (myState) {
     case S0: if  (n) myState = S5;
              else 
              if (d) myState = S10;
              break;
     case S5: if (n) myState = S10;
              else 
              if (d) myState = S15;
              break;
             
     case S10: if (n) myState = S15;
               else 
               if (d) myState = S20;
               break;
             
     case S15: if (sampletime>=6) {
                myState = S0;sampletime=0;}
               else{
                sampletime++;
               }
               break;
     case S20: if (sampletime>=3) {
               myState = S15;sampletime=0;}
               else{
                sampletime++;
               }
               break;
  
     default: myState=S0;
}

     switch (myState) {
     case S0: digitalWrite(12,0); break;
     case S5:
     case S10: R=0; C=0; break;
     case S15: R=1; C=0;digitalWrite(12,1);digitalWrite(13,0); break;
     case S20: R=0; C=1;digitalWrite(13,1);
    
     default: R=0; C=0; // This should never happen!
}
}

void Determine_n_d(void)
 {
  static int previousread2=1, previousread3=1;
  static int currentread2=1, currentread3=1;

     previousread2 = currentread2;
     previousread3 = currentread3; 
     currentread3 = digitalRead(3);
     currentread2 = digitalRead(2);
  
    
     
     if  ((previousread2==1) && (currentread2==0))
        n=1;
     else 
        n=0;
     if  ((previousread3==1) && (currentread3==0))
        d=1;
     else 
        d=0;
   
 }
 
 void steit(){ 
 switch (myStates) {
     case Off0: if (digitalRead(7)==LOW){
      digitalWrite(10, 0), myStates=On1;
     }
     break;

     case On1: if (digitalRead(7)==HIGH){
      digitalWrite(10, 1), myStates=On2;
     }
     break;

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
