#include<SPI.h>
#include<MFRC522.h>
#define RST_PIN 9
#define SS_PIN 10

MFRC522 rfid(SS_PIN, RST_PIN);
String uidString;
int k=0;
void setup(){
  Serial.begin(9600);
  while(!Serial); // for Leonardo/Micro/Zero
  
  // Init SPI bus
  SPI.begin(); 
  // Init MFRC522 
  rfid.PCD_Init(); 
  rfid.PCD_DumpVersionToSerial();  // Show details of PCD - MFRC522 Card Reader details
}
void loop() {
if(rfid.PICC_IsNewCardPresent())
{
  readRFID();
  k=k+1;
}

}
void readRFID() {
  rfid.PICC_ReadCardSerial();
  delay(100);
  uidString = String(rfid.uid.uidByte[0]) + " " + String(rfid.uid.uidByte[1]) + " " + 
    String(rfid.uid.uidByte[2]) + " " + String(rfid.uid.uidByte[3]);
 
  // Sound the buzzer when a card i      
  if (k>1){
  Serial.println(uidString);}
}
