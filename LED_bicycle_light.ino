#define Off 2
#define A 32
#define On1 43
#define Off1 20
#define B 23
#define On2 36
#define Off2 51
#define C 96
#define On 35
#define D 45
#define On3 27
#define Off3 95
#define E 333

int states=Off, timer=0, brightness=0, fadeAmount = 5;

void setup() {
  pinMode(6, OUTPUT);
  pinMode(8, INPUT_PULLUP);
  Serial.print(9600);
}

void loop() {
 lights();
 delay(5);
}

void lights(){
  switch(states){
    
    case Off: if(digitalRead(8)==LOW){
      states=A;}
          break;
    case A:   if(digitalRead(8)==HIGH){
      digitalWrite(6,1), states=On1;}
          break;
    case On1: if(digitalRead(8)==LOW){
      states=B;}
              else
              if(timer>=80){
                digitalWrite(6,1);
                states=Off1;
                timer=0;}
              else{
                timer++;
              }
          break;    
    case Off1: if(timer>=80){
                digitalWrite(6,0);
                states=On1; 
                timer=0;}
              else{
                timer++;
              }
              break;
    case B:   if(digitalRead(8)==HIGH){
      digitalWrite(6,1), states=On2;}
              break;
    case On2: if(digitalRead(8)==LOW){
      states=C;}
              else
              if(timer>=20){
                digitalWrite(6,1);
                states=Off2;
                timer=0;}
              else{
                timer++;
              }
             break;
    case Off2: if(timer>=20){
      digitalWrite(6,0);
                states=On2; 
                timer=0;}
              else{
                timer++;}
              break;
    case C:   if(digitalRead(8)==HIGH){
      digitalWrite(6,1), states=On;}
              break;
         
    case On:  if(digitalRead(8)==LOW){
      digitalWrite(6,0), states=D;}
              break;
              
    case D:   if(digitalRead(8)==HIGH){
      digitalWrite(6,1), states=On3;}
              break;
                
    case On3: if(digitalRead(8)==LOW){
      states=E;}
              else
              if(timer>=1){
                digitalWrite(6,1);
                states=Off3;
                timer=0;}
              else{
                timer++;
              }
             break; 
    case Off3: if(timer>=1){
                digitalWrite(6,0);
                states=On3; 
                timer=0;}
               else{
                timer++;}
               break;          
    case E: if(digitalRead(8)==HIGH){
      digitalWrite(6,0), states=Off;}
              break;                   
    
    default: states=Off;
}
}
