#include <stdlib.h>

char serial;
#define RELAY1  7                       
void setup()
{   
  Serial.begin(9600);
  pinMode(RELAY1, OUTPUT);       
}

void loop()
{
        Serial.println("6567t7t8t78t");
}
