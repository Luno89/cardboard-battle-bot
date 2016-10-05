String incoming = "";
Boolean completeString = false;

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  if(completeString)
  {
    triggerEvent(incoming);
    completeString = false;
    incoming = "";
  }
}

void serialEvent()
{
  while(Serial.available() > 0) {
    char inchar = (char)Serial.read();
    
    if (inchar == '\n;) {
      completeString = true;
    } else {
      incoming = incoming + inchar;
    }
  }
}
